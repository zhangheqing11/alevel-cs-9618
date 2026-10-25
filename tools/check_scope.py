#!/usr/bin/env python3
"""`make check-scope TASK=Txx`: fail if this branch touches files outside the task's allowed globs.

Allowed globs live in tasks/scope.json: {"T12": {"allow": ["pipeline/extract/**", ...]}}.
`**` matches across directories, `*` within one path segment.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def glob_to_regex(pattern: str) -> re.Pattern:
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out += r"(?:.*/)?"
            i += 3
        elif pattern.startswith("**", i):
            out += r".*"
            i += 2
        elif pattern[i] == "*":
            out += r"[^/]*"
            i += 1
        elif pattern[i] == "?":
            out += r"[^/]"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile(out + r"\Z")


def git(*args: str) -> str:
    return subprocess.run(["git", "-c", "core.quotepath=false", *args], cwd=ROOT, capture_output=True, text=True).stdout


def changed_files() -> list[str]:
    base = ""
    for ref in ("origin/main", "main"):
        base = git("merge-base", ref, "HEAD").strip()
        if base:
            break
    files = set(git("diff", "--name-only", base, "HEAD").splitlines()) if base else set()
    for line in git("status", "--porcelain", "--untracked-files=all").splitlines():
        files.add(line[3:].strip().strip('"'))
    return sorted(f for f in files if f)


def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1]:
        print("usage: make check-scope TASK=Txx")
        return 2
    task = sys.argv[1]
    scope = json.loads((ROOT / "tasks" / "scope.json").read_text(encoding="utf-8"))
    if task not in scope:
        print(f"✗ {task} not in tasks/scope.json")
        return 2
    allowed = [glob_to_regex(g) for g in scope[task]["allow"]] + [glob_to_regex(f"tasks/progress/{task}.md")]
    bad = [f for f in changed_files() if not any(r.match(f) for r in allowed)]
    if bad:
        print(f"✗ {task} touches files outside its scope:")
        for f in bad:
            print(f"  - {f}")
        print("Move the change into scope, or ask 总控 (write 「需要总控决定」 in the PR).")
        return 1
    print(f"✓ {task}: all changed files are in scope")
    return 0


if __name__ == "__main__":
    sys.exit(main())
