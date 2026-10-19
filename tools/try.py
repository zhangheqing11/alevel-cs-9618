#!/usr/bin/env python3
"""`make try EX=<exercise dir> [K=<pytest -k expr>]`: test the learner's attempt for one exercise.

First run creates attempts/<EX>/solution.py from starter.py (and answer.pseudo /
answer.steps.md when the exercise has them) and tells the learner where to write.
Data files under <EX>/files/ are copied next to solution.py (never overwriting the
learner's copies), so `python solution.py` can open them by relative name (P4).
K narrows the run to matching tests, e.g. `make try EX=… K=1b` (one sub-question).
"""
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) not in (2, 3) or not sys.argv[1]:
        print("usage: make try EX=practice/p2/<exercise> [K=<test filter>]  or  EX=ladder/levels/L01-…/exercises/E01-…")
        return 2
    keyword = sys.argv[2].strip() if len(sys.argv) == 3 else ""
    ex = (ROOT / sys.argv[1]).resolve()
    if not (ex / "test_task.py").exists():
        print(f"✗ no exercise at {sys.argv[1]}")
        return 2
    attempt_dir = ROOT / "attempts" / ex.relative_to(ROOT)
    solution = attempt_dir / "solution.py"
    created = not solution.exists()
    attempt_dir.mkdir(parents=True, exist_ok=True)
    copied = copy_data_files(ex, attempt_dir)
    if created:
        shutil.copy(ex / "starter.py", solution)
        for extra in ("answer.pseudo", "answer.steps.md"):
            if (ex / extra).exists() and not (attempt_dir / extra).exists():
                shutil.copy(ex / extra, attempt_dir / extra)
        print(f"Created {solution.relative_to(ROOT)} — write your answer there, then run `make try` again.")
        if copied:
            print(f"Copied data files next to it: {', '.join(copied)}")
        return 0
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("CANDIDATE", None)
    cmd = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", str(ROOT),
           str(ex / "test_task.py")]
    if keyword:
        cmd += ["-k", keyword]
    return subprocess.run(cmd, cwd=ROOT, env=env).returncode


def copy_data_files(ex: pathlib.Path, attempt_dir: pathlib.Path) -> list[str]:
    """Copy <ex>/files/* into the attempt folder byte for byte; keep existing copies."""
    src = ex / "files"
    copied = []
    if src.is_dir():
        for f in sorted(src.rglob("*")):
            if f.is_file():
                dest = attempt_dir / f.relative_to(src)
                if not dest.exists():
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(f, dest)
                    copied.append(str(f.relative_to(src)))
    return copied


if __name__ == "__main__":
    sys.exit(main())
