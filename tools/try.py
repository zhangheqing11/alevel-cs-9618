#!/usr/bin/env python3
"""`make try EX=<exercise dir>`: test the learner's attempt for one exercise.

First run creates attempts/<EX>/solution.py from starter.py (and answer.pseudo
when the exercise needs pseudocode) and tells the learner where to write.
"""
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1]:
        print("usage: make try EX=practice/p2/<exercise>  or  EX=ladder/levels/L01-…/exercises/E01-…")
        return 2
    ex = (ROOT / sys.argv[1]).resolve()
    if not (ex / "test_task.py").exists():
        print(f"✗ no exercise at {sys.argv[1]}")
        return 2
    attempt_dir = ROOT / "attempts" / ex.relative_to(ROOT)
    solution = attempt_dir / "solution.py"
    if not solution.exists():
        attempt_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(ex / "starter.py", solution)
        if (ex / "answer.pseudo").exists():
            shutil.copy(ex / "answer.pseudo", attempt_dir / "answer.pseudo")
        print(f"Created {solution.relative_to(ROOT)} — write your answer there, then run `make try` again.")
        return 0
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("CANDIDATE", None)
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", str(ROOT),
         str(ex / "test_task.py")], cwd=ROOT, env=env,
    ).returncode


if __name__ == "__main__":
    sys.exit(main())
