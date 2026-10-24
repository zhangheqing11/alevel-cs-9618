#!/usr/bin/env python3
"""Print the syllabus-section → paper → chapter → type-code table (markdown) from papers/p<N>/taxonomy.json.

  syllabus_map.py              # all four papers
  syllabus_map.py P3 P4        # only these papers

Each type's own `syllabus` field decides where it is listed (a type with two sections appears under both).
The output is pasted into references/syllabus-map.md §5; rerun it when a taxonomy changes.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from collections import defaultdict


def find_root() -> pathlib.Path:
    here = pathlib.Path.cwd().resolve()
    for p in (here, *here.parents):
        if (p / "AGENTS.md").exists() and (p / "schemas").is_dir():
            return p
    sys.exit("✗ run from inside the repo")


def section_key(s: str) -> tuple[int, ...]:
    return tuple(int(x) for x in s.split("."))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("papers", nargs="*", default=["P1", "P2", "P3", "P4"])
    args = ap.parse_args(argv)
    root = find_root()
    table: dict[str, dict[tuple[str, str], list[str]]] = defaultdict(lambda: defaultdict(list))
    for paper in args.papers:
        n = paper.upper().lstrip("P")
        tax = json.loads((root / "papers" / f"p{n}" / "taxonomy.json").read_text(encoding="utf-8"))
        names = {c["code"]: c["name_zh"] for c in tax["chapters"]}
        for t in tax["types"]:
            for sec in t["syllabus"]:
                table[sec][(f"P{n}", f"{t['chapter']} {names[t['chapter']]}")].append(t["code"])
    print("| 考纲 | 卷 | 章 | 题型码 |")
    print("|:--|:--|:--|:--|")
    for sec in sorted(table, key=section_key):
        for (paper, chapter), codes in sorted(table[sec].items()):
            short = [c.split("-", 1)[1] for c in codes]
            print(f"| {sec} | {paper} | {chapter} | {'、'.join(short)} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
