"""Helpers for exercise tests (see schemas/exercise-format.md)."""
from __future__ import annotations

import builtins
import dataclasses
import pathlib
import shutil
import subprocess
import sys
import tempfile


def output_lines(text: str) -> list[str]:
    """Split captured stdout into comparable lines: strip trailing spaces, drop blank lines.

    Same rule as ScriptResult.lines; use with capsys for io/trace-style tests:
        sol.rogue_average(); assert output_lines(capsys.readouterr().out) == [...]
    """
    return [ln.rstrip() for ln in text.splitlines() if ln.strip()]


@dataclasses.dataclass
class ScriptResult:
    stdout: str
    stderr: str
    returncode: int
    workdir: pathlib.Path

    @property
    def lines(self) -> list[str]:
        """Non-empty stdout lines with trailing spaces stripped."""
        return output_lines(self.stdout)

    def read(self, name: str) -> str:
        """Contents of a file the script wrote (or left) in its working directory."""
        return (self.workdir / name).read_text(encoding="utf-8")


def run_script(path, stdin: str = "", files_dir=None, args=(), timeout: float = 5.0) -> ScriptResult:
    """Run a candidate program as `python <path>` inside a fresh temp directory.

    files_dir: a directory whose contents are copied into the working directory
    first (normally <exercise>/files). stdin is fed verbatim; end lines with \\n.
    """
    workdir = pathlib.Path(tempfile.mkdtemp(prefix="run_"))
    if files_dir is not None and pathlib.Path(files_dir).is_dir():
        shutil.copytree(files_dir, workdir, dirs_exist_ok=True)
    proc = subprocess.run(
        [sys.executable, str(pathlib.Path(path).resolve()), *args],
        input=stdin, capture_output=True, text=True, cwd=workdir, timeout=timeout,
    )
    return ScriptResult(proc.stdout, proc.stderr, proc.returncode, workdir)


def feed_input(monkeypatch, *answers: str) -> None:
    """Make builtins.input() return the given answers in order (for function-style tests)."""
    queue = list(answers)

    def fake_input(prompt: str = "") -> str:
        if not queue:
            raise AssertionError("program asked for more input than the test provides")
        return queue.pop(0)

    monkeypatch.setattr(builtins, "input", fake_input)


def use_files(monkeypatch, tmp_path, files_dir) -> pathlib.Path:
    """Copy <exercise>/files into tmp_path and chdir there, for function-style tests
    whose code opens data files by relative name (P4: "QueueData.txt").

    Call it before invoking the function under test; returns the working directory
    so the test can read files the program wrote:
        work = use_files(monkeypatch, tmp_path, exercise_dir / "files")
        sol.ReadData(); assert (work / "Out.txt").read_text() == ...
    """
    src = pathlib.Path(files_dir)
    if src.is_dir():
        shutil.copytree(src, tmp_path, dirs_exist_ok=True)
    monkeypatch.chdir(tmp_path)
    return pathlib.Path(tmp_path)
