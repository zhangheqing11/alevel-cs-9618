"""Test-only adapters for T25; candidates never import this module."""
import ast
import importlib.util
import itertools
import shutil

_counter = itertools.count()


def load_at(candidate_path, exercise_dir, tmp_path, monkeypatch):
    """Load the fixture-selected candidate in an isolated copy of files/."""
    source = exercise_dir / 'files'
    if source.is_dir():
        shutil.copytree(source, tmp_path, dirs_exist_ok=True)
    monkeypatch.chdir(tmp_path)
    spec = importlib.util.spec_from_file_location(f'file_candidate_{next(_counter)}', candidate_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def watch_open(monkeypatch):
    """Keep handles alive so a forgotten CLOSEFILE cannot be hidden by GC."""
    import builtins
    import io
    original = builtins.open
    handles = []

    def tracked(*args, **kwargs):
        handle = original(*args, **kwargs)
        handles.append(handle)
        return handle

    monkeypatch.setattr(builtins, 'open', tracked)
    monkeypatch.setattr(io, 'open', tracked)
    return handles


def no_shortcuts(candidate_path):
    """Enforce only the explicitly prohibited lookup/sort shortcuts (D10).

    All loop, indexing and helper choices remain free. This is a separate
    requirement check, not an assertion of one particular implementation.
    """
    tree = ast.parse(candidate_path.read_text(encoding='utf-8'))
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            assert not any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops), 'Use the requested search algorithm, not membership lookup'
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                assert node.func.attr not in {'sort', 'index'}, 'Use the requested algorithm, not sort()/index()'
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {'sorted', 'max', 'min'}, 'Use the requested algorithm, not a built-in replacement'
