#!/usr/bin/env python3
"""Check that, compared with a base git revision, only T34-owned fields changed in corpus/rows/p4.

For every row the non-owned members must be byte-identical and in the same order (D33).
Usage: audit_merge.py [--base origin/main]
"""
import argparse
import json
import subprocess

from apply_p4 import OWNED, ROOT, ROWS, top_level_spans


def members(line):
    spans, _ = top_level_spans(line)
    return [line[s:e] for key, s, e in spans if key not in OWNED]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main")
    args = parser.parse_args()
    rows = files = 0
    for path in sorted(ROWS.glob("*.jsonl")):
        rel = path.relative_to(ROOT).as_posix()
        base = subprocess.run(["git", "show", f"{args.base}:{rel}"], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.splitlines()
        now = path.read_text(encoding="utf-8").splitlines()
        if len(base) != len(now):
            raise SystemExit(f"{rel}: line count changed")
        for old, new in zip(base, now):
            if members(old) != members(new) or json.loads(old)["id"] != json.loads(new)["id"]:
                raise SystemExit(f"{rel}: non-owned bytes changed in {json.loads(old)['id']}")
            rows += 1
        files += 1
    print(f"{files} files, {rows} rows: non-owned fields byte-identical to {args.base}")


if __name__ == "__main__":
    main()
