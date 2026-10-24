#!/usr/bin/env python3
"""Create a paper's empty mastery ledger from its taxonomy and built index.

  init_ledger.py P3            # writes ledger/P3.csv (refuses to overwrite)
  init_ledger.py P4 --force    # rebuild even if ledger/P4.csv exists (loses progress!)
  init_ledger.py P2 --out work/tmp/P2_check.csv   # write elsewhere, e.g. to diff against the real one

One row per type in papers/p<N>/taxonomy.json order: 类型, 名称 (name_zh), 章节 ("<code> <chapter name_zh>"),
优先级 (stars from output/p<N>/index.json — run `python3 build/build.py all` first), 状态=未学, other columns empty.
Format: schemas/ledger-format.md (13 columns, utf-8-sig, CRLF like the existing ledgers).
Existing ledgers are the learner's real records: never overwrite them without --force, and never use --force
on a ledger that already has progress (the script refuses if any 状态 is not 未学 unless --force-progress).
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys

COLS = ["类型", "名称", "章节", "优先级", "状态", "日期", "独立题目", "得分", "错误类别", "失分技能",
        "解释证据", "复测日期", "复测结果"]
PAPERS = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}


def find_root(explicit: str | None) -> pathlib.Path:
    if explicit:
        return pathlib.Path(explicit).resolve()
    here = pathlib.Path.cwd().resolve()
    for p in (here, *here.parents):
        if (p / "AGENTS.md").exists() and (p / "schemas").is_dir():
            return p
    sys.exit("✗ cannot find the repo root (a folder with AGENTS.md); run from the repo or pass --root")


def build_rows(root: pathlib.Path, n: int) -> list[dict]:
    tax_path = root / "papers" / f"p{n}" / "taxonomy.json"
    idx_path = root / "output" / f"p{n}" / "index.json"
    if not tax_path.exists():
        sys.exit(f"✗ {tax_path.relative_to(root)} missing: this paper's taxonomy is not merged yet")
    if not idx_path.exists():
        sys.exit(f"✗ {idx_path.relative_to(root)} missing: run `python3 build/build.py all` (or `make build`) first")
    tax = json.loads(tax_path.read_text(encoding="utf-8"))
    idx = json.loads(idx_path.read_text(encoding="utf-8"))["types"]
    chapters = {c["code"]: f"{c['code']} {c['name_zh']}" for c in tax["chapters"]}
    rows = []
    for t in tax["types"]:
        code = t["code"]
        if code not in idx:
            sys.exit(f"✗ {code} is in taxonomy.json but not in index.json: rebuild output/ first")
        stars = idx[code].get("stars") or ""
        if not stars:
            sys.exit(f"✗ {code} has no stars in index.json")
        row = {c: "" for c in COLS}
        row.update({"类型": code, "名称": t["name_zh"], "章节": chapters[t["chapter"]], "优先级": stars,
                    "状态": "未学"})
        rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paper", choices=sorted(PAPERS), help="P1 / P2 / P3 / P4")
    ap.add_argument("--root", help="repo root (default: nearest folder with AGENTS.md)")
    ap.add_argument("--out", help="write here instead of ledger/<paper>.csv")
    ap.add_argument("--force", action="store_true", help="overwrite an existing ledger that has no progress")
    ap.add_argument("--force-progress", action="store_true",
                    help="overwrite even if the ledger has progress (destroys the learner's record)")
    args = ap.parse_args(argv)
    root = find_root(args.root)
    target = pathlib.Path(args.out).resolve() if args.out else root / "ledger" / f"{args.paper}.csv"
    if target.exists():
        if not (args.force or args.force_progress):
            print(f"{target.relative_to(root) if target.is_relative_to(root) else target} already exists — "
                  "not overwritten (pass --force to rebuild an untouched ledger)")
            return 0
        with target.open(encoding="utf-8-sig", newline="") as f:
            started = [r["类型"] for r in csv.DictReader(f) if r.get("状态", "未学") not in ("", "未学")]
        if started and not args.force_progress:
            sys.exit(f"✗ {target.name} already has progress ({len(started)} types, e.g. {started[0]}); refusing")
    rows = build_rows(root, PAPERS[args.paper])
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLS)          # default lineterminator \r\n, like P1/P2.csv
        writer.writeheader()
        writer.writerows(rows)
    chapters = len({r["章节"] for r in rows})
    print(f"wrote {target}: {len(rows)} types in {chapters} chapters, all 未学")
    return 0


if __name__ == "__main__":
    sys.exit(main())
