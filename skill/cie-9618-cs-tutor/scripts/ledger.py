#!/usr/bin/env python3
"""Read and update the learner's mastery ledgers (ledger/*.csv, utf-8-sig).

  ledger.py summary
      status counts per ledger, the 学习中 list, retests that are due
  ledger.py show P1 [--status 学习中] [--chapter IR] [--code P1-IR-03]
  ledger.py set P1 P1-IR-03 状态=学习中 得分=2/3 独立题目+=9618_s24_12:2(a) 错误类别+=手算与单位

`列=值` replaces a cell; `列+=值` appends to a ；-separated list without duplicates.
Changing 状态 sets 日期 to today unless 日期= is also given. Ledger names: P1 P2 P3 P4 ladder.
Run from the repo root, or pass --root. Column layout: schemas/ledger-format.md.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import pathlib
import re
import sys
import tempfile

COLS = ["类型", "名称", "章节", "优先级", "状态", "日期", "独立题目", "得分", "错误类别", "失分技能",
        "解释证据", "复测日期", "复测结果"]
STATUSES = ["未学", "学习中", "已掌握"]
ERROR_CATEGORIES = ["概念", "题型识别", "算法设计", "伪代码规范", "边界与差一", "数据结构", "文件处理",
                    "类型与转换", "手算与单位", "考试措辞", "漏 MS 得分点", "测试与调试", "综合迁移"]
LEDGERS = {"P1": "P1.csv", "P2": "P2.csv", "P3": "P3.csv", "P4": "P4.csv", "LADDER": "ladder.csv"}
LIST_COLS = ("独立题目", "错误类别", "失分技能")
SEP = "；"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ASSIGN_RE = re.compile(r"^([^=+]+?)(\+?=)(.*)$", re.S)


class LedgerError(Exception):
    pass


def find_root(explicit: str | None) -> pathlib.Path:
    if explicit:
        return pathlib.Path(explicit).resolve()
    here = pathlib.Path.cwd().resolve()
    for p in (here, *here.parents):
        if (p / "AGENTS.md").exists() and (p / "schemas").is_dir():
            return p
    raise LedgerError("cannot find the repo root (a folder with AGENTS.md); run from the repo or pass --root")


def ledger_path(root: pathlib.Path, name: str) -> pathlib.Path:
    key = name.upper()
    if key in ("L", "LAD"):
        key = "LADDER"
    if key not in LEDGERS:
        raise LedgerError(f"unknown ledger {name!r}; use one of P1 P2 P3 P4 ladder")
    return root / "ledger" / LEDGERS[key]


def read_ledger(path: pathlib.Path) -> tuple[list[dict], str]:
    if not path.exists():
        raise LedgerError(f"{path} does not exist yet (总控 creates it from taxonomy.json)")
    raw = path.read_bytes()
    newline = "\r\n" if b"\r\n" in raw else "\n"
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLS:
            raise LedgerError(f"{path}: header {reader.fieldnames} != expected {COLS}")
        rows = [dict(r) for r in reader]
    return rows, newline


def write_ledger(path: pathlib.Path, rows: list[dict], newline: str) -> None:
    fd, tmp = tempfile.mkstemp(prefix=".ledger_", suffix=".csv", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLS, lineterminator=newline)
            writer.writeheader()
            for r in rows:
                writer.writerow({c: r.get(c, "") for c in COLS})
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def split_list(cell: str) -> list[str]:
    return [x.strip() for x in re.split(r"[；;]", cell or "") if x.strip()]


def canonical_category(value: str) -> str:
    squash = value.replace(" ", "").replace("　", "")
    for cat in ERROR_CATEGORIES:
        if cat.replace(" ", "") == squash:
            return cat
    raise LedgerError(f"unknown 错误类别 {value!r}; allowed: {'、'.join(ERROR_CATEGORIES)}")


def skill_vocab(root: pathlib.Path, ledger_name: str) -> set[str] | None:
    """Allowed 失分技能 tags for this ledger, or None when no vocabulary exists yet."""
    papers = {"P2": ["p2"], "P4": ["p2", "p4"], "LADDER": ["p2", "p4"]}.get(ledger_name.upper())
    if not papers:
        return None
    tags: set[str] = set()
    found = False
    for p in papers:
        f = root / "papers" / p / "skill_tags.json"
        if f.exists():
            found = True
            tags |= {t["tag"] for t in json.loads(f.read_text(encoding="utf-8")).get("tags", [])}
    if ledger_name.upper() == "LADDER":
        for meta in (root / "ladder").rglob("meta.json") if (root / "ladder").is_dir() else []:
            found = True
            tags |= set(json.loads(meta.read_text(encoding="utf-8")).get("skills", []))
    return tags if found else None


def apply_assignments(row: dict, assignments: list[str], root: pathlib.Path, ledger_name: str,
                      force: bool) -> list[str]:
    changed: list[str] = []
    date_given = False
    vocab = None if force else skill_vocab(root, ledger_name)
    for a in assignments:
        m = ASSIGN_RE.match(a)
        if not m:
            raise LedgerError(f"cannot parse {a!r}; use 列=值 or 列+=值")
        col, op, value = m.group(1).strip(), m.group(2), m.group(3).strip()
        if col not in COLS:
            raise LedgerError(f"unknown column {col!r}; columns: {' '.join(COLS)}")
        if col in ("类型", "名称", "章节", "优先级"):
            raise LedgerError(f"{col} is maintained by 总控; the learning session does not change it")
        if col == "状态" and value not in STATUSES:
            raise LedgerError(f"状态 must be one of {STATUSES}")
        if col in ("日期", "复测日期") and value and not DATE_RE.match(value):
            raise LedgerError(f"{col} must be YYYY-MM-DD, got {value!r}")
        if col in LIST_COLS:
            new_items = split_list(value)
            if col == "错误类别":
                new_items = [canonical_category(x) for x in new_items]
            if col == "失分技能" and vocab is not None:
                unknown = [x for x in new_items if x not in vocab]
                if unknown:
                    raise LedgerError(f"失分技能 not in the skill-tag vocabulary: {unknown} (use --force only "
                                      "for a vocabulary gap you also report in handoff/勘误.md)")
            items = split_list(row[col]) if op == "+=" else []
            items += [x for x in new_items if x not in items]
            new_value = SEP.join(items)
        elif op == "+=" and row[col] and value:
            new_value = row[col] if value in row[col] else row[col] + SEP + value
        else:
            new_value = value
        if col == "日期":
            date_given = True
        if new_value != row[col]:
            if col == "状态" and not date_given:
                row["日期"] = dt.date.today().isoformat()
            row[col] = new_value
            changed.append(col)
    return changed


def cmd_set(args) -> int:
    root = find_root(args.root)
    path = ledger_path(root, args.ledger)
    rows, newline = read_ledger(path)
    matches = [r for r in rows if r["类型"] == args.code]
    if not matches:
        raise LedgerError(f"{args.code} not found in {path.name}")
    row = matches[0]
    changed = apply_assignments(row, args.assignments, root, args.ledger, args.force)
    if changed:
        write_ledger(path, rows, newline)
    print(f"{path.name} {args.code}: " + ("updated " + ", ".join(changed) if changed else "no change"))
    print_rows([row], full=True)
    return 0


def print_rows(rows: list[dict], full: bool = False) -> None:
    for r in rows:
        head = f"{r['类型']}  {r['名称']}  [{r['状态'] or '—'}]"
        if r["优先级"]:
            head += f"  {r['优先级']}"
        print(head)
        for c in COLS[5:] if full else ["日期", "得分", "错误类别", "失分技能", "解释证据", "复测日期"]:
            if r.get(c):
                print(f"    {c}: {r[c]}")


def cmd_show(args) -> int:
    root = find_root(args.root)
    path = ledger_path(root, args.ledger)
    rows, _ = read_ledger(path)
    sel = rows
    if args.status:
        sel = [r for r in sel if r["状态"] == args.status]
    if args.chapter:
        sel = [r for r in sel if r["章节"].startswith(args.chapter) or f"-{args.chapter}-" in r["类型"]]
    if args.code:
        sel = [r for r in sel if r["类型"] == args.code]
    if args.csv:
        w = csv.DictWriter(sys.stdout, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows(sel)
    else:
        print_rows(sel, full=bool(args.code))
        print(f"({len(sel)} of {len(rows)} rows)")
    return 0


def cmd_summary(args) -> int:
    root = find_root(args.root)
    today = dt.date.today().isoformat()
    any_found = False
    for key, fname in LEDGERS.items():
        path = root / "ledger" / fname
        if not path.exists():
            print(f"{fname}: (not created yet)")
            continue
        any_found = True
        rows, _ = read_ledger(path)
        counts = {s: sum(r["状态"] == s for r in rows) for s in STATUSES}
        blank = sum(r["状态"] == "" for r in rows)
        line = f"{fname}: " + " / ".join(f"{s} {counts[s]}" for s in reversed(STATUSES))
        if blank:
            line += f" / 空 {blank}"
        print(line)
        learning = [r for r in rows if r["状态"] == "学习中"]
        for r in learning:
            due = r["复测日期"]
            flag = "  ⚠ 到期" if due and due <= today and not r["复测结果"] else ""
            print(f"    学习中 {r['类型']} {r['名称']}" + (f"（复测 {due}）" if due else "") + flag)
        last = max((r["日期"] for r in rows if r["日期"]), default="")
        if last:
            print(f"    最近更新 {last}")
    if not any_found:
        print("No ledgers yet: they are generated by 总控 when a paper's taxonomy is merged.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", help="repo root (default: nearest folder with AGENTS.md)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("summary", help="status counts, 学习中 list, due retests")
    p = sub.add_parser("show", help="print rows of one ledger")
    p.add_argument("ledger")
    p.add_argument("--status", choices=STATUSES)
    p.add_argument("--chapter", help="chapter code, e.g. IR")
    p.add_argument("--code", help="one type code / ladder level")
    p.add_argument("--csv", action="store_true")
    p = sub.add_parser("set", help="update cells of one row")
    p.add_argument("ledger")
    p.add_argument("code")
    p.add_argument("assignments", nargs="+", help="列=值 or 列+=值")
    p.add_argument("--force", action="store_true", help="accept 失分技能 tags missing from the vocabulary")
    args = ap.parse_args(argv)
    try:
        return {"summary": cmd_summary, "show": cmd_show, "set": cmd_set}[args.cmd](args)
    except LedgerError as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
