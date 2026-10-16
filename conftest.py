"""Shared pytest fixtures for exercise folders (see schemas/exercise-format.md).

Tests never import the learner's code directly. They declare a `sol` parameter
(for function-style tasks) or `candidate_path` (for script-style tasks run via
tools/testkit.run_script). The candidate file is chosen in this order:
  1. $CANDIDATE (used by `make check` for ref/solution.py and mutants)
  2. attempts/<exercise dir relative to repo root>/solution.py
  3. otherwise the test is skipped.
"""
import importlib.util
import itertools
import os
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))

_counter = itertools.count()


def _exercise_dir(request) -> pathlib.Path:
    return pathlib.Path(str(request.node.fspath)).resolve().parent


def _resolve_candidate(exercise_dir: pathlib.Path) -> pathlib.Path:
    env = os.environ.get("CANDIDATE")
    if env:
        return pathlib.Path(env).resolve()
    return ROOT / "attempts" / exercise_dir.relative_to(ROOT) / "solution.py"


def load_module(path: pathlib.Path):
    """Import a Python file as a fresh module (no caching between tests)."""
    name = f"candidate_{next(_counter)}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(path.parent))
    return module


@pytest.fixture
def exercise_dir(request) -> pathlib.Path:
    return _exercise_dir(request)


@pytest.fixture
def candidate_path(request) -> pathlib.Path:
    path = _resolve_candidate(_exercise_dir(request))
    if not path.exists():
        pytest.skip(f"no candidate file at {path} (run `make try EX=...` first)")
    return path


@pytest.fixture
def sol(candidate_path, exercise_dir, monkeypatch):
    """The candidate module, freshly imported, with cwd set to a copy of files/."""
    files = exercise_dir / "files"
    if files.is_dir():
        import shutil
        import tempfile
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="ex_"))
        shutil.copytree(files, tmp, dirs_exist_ok=True)
        monkeypatch.chdir(tmp)
    return load_module(candidate_path)
