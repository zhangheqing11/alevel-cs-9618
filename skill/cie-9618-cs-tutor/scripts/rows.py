#!/usr/bin/env python3
"""Look up past-paper leaves (corpus/rows) and their source PDFs for a study session.

  rows.py get 9618_s24_22:6(a) [--ms] [--json]
      stem, context, marks, pages, flags; the MS text and mark points only with --ms
  rows.py files 9618_s24_22[:6(a)]
      absolute paths of that paper's QP / MS / insert / examiner report / thresholds / P4 source files
  rows.py render 9618_s24_22:6(a) [--ms] [--pages 2] [--dpi 110] [--out work/tmp/figures]
      render the QP (or MS) page(s) of a leaf to PNG
  rows.py drills P2-XX-04 [--all]
      verified-corpus leaves whose primary type is this code, newest first; marks done / duplicate /
      reserved (s26) items; 2021 extension leaves listed after
  rows.py find [--paper 9618_s24_22] [--type P2-XX-04] [--skill file-close] [--grep TEXT] [--ms]
  rows.py ex 9618_s24_22:6(a)
      practice folders whose meta.json covers this leaf

Default: never print MS text unless --ms is given (the learner must not see it before answering).
Run from the repo root, or pass --root. Sources: $ALEVEL_CS_SOURCES or the default path below.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import pathlib
import re
import sys
import textwrap

DEFAULT_SOURCES = "/Users/zhangheqing/Desktop/alevel cs/sources"
RESERVED_SESSIONS = {("s", 2026)}          # kept for timed full papers in the sprint (SKILL.md §3.5)
SESSION_ORDER = {"m": 1, "s": 2, "w": 3}
PAPER_RE = re.compile(r"^9618_([msw])(\d{2})_([1-4])([1-3])$")
LEDGER_FILES = {1: "P1.csv", 2: "P2.csv", 3: "P3.csv", 4: "P4.csv"}


class RowsError(Exception):
    pass


# ------------------------------------------------------------------ locating things

def find_root(explicit: str | None) -> pathlib.Path:
    if explicit:
        return pathlib.Path(explicit).resolve()
    here = pathlib.Path.cwd().resolve()
    for p in (here, *here.parents):
        if (p / "AGENTS.md").exists() and (p / "schemas").is_dir():
            return p
    raise RowsError("cannot find the repo root (a folder with AGENTS.md); run from the repo or pass --root")


def sources_dir() -> pathlib.Path:
    return pathlib.Path(os.environ.get("ALEVEL_CS_SOURCES", DEFAULT_SOURCES))


def parse_paper(paper: str) -> dict:
    m = PAPER_RE.match(paper)
    if not m:
        raise RowsError(f"not a paper code: {paper!r} (expected e.g. 9618_s24_22)")
    return {"session": m.group(1), "year": 2000 + int(m.group(2)), "component": int(m.group(3)),
            "variant": int(m.group(4))}


def split_id(row_id: str) -> tuple[str, str | None]:
    paper, _, q = row_id.partition(":")
    parse_paper(paper)
    return paper, (q or None)


def short_ref(row_id: str) -> str:
    """9618_s24_22:3(b)(ii) -> s24/22 Q3(b)(ii)"""
    paper, q = split_id(row_id)
    m = PAPER_RE.match(paper)
    ref = f"{m.group(1)}{m.group(2)}/{m.group(3)}{m.group(4)}"
    return f"{ref} Q{q}" if q else ref


def inventory(root: pathlib.Path) -> dict[str, dict]:
    path = root / "corpus" / "inventory.csv"
    if not path.exists():
        raise RowsError("corpus/inventory.csv missing")
    with path.open(encoding="utf-8-sig", newline="") as f:
        return {r["paper"]: r for r in csv.DictReader(f)}


def load_paper_rows(root: pathlib.Path, paper: str) -> list[dict]:
    comp = parse_paper(paper)["component"]
    path = root / "corpus" / "rows" / f"p{comp}" / f"{paper}.jsonl"
    if not path.exists():
        raise RowsError(f"no rows for {paper} yet ({path.relative_to(root)} missing) — read the PDF directly "
                        f"(rows.py files {paper})")
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def all_rows(root: pathlib.Path, component: int | None = None):
    base = root / "corpus" / "rows"
    dirs = [base / f"p{component}"] if component else sorted(base.glob("p[1-4]"))
    for d in dirs:
        for path in sorted(d.glob("*.jsonl")):
            with path.open(encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        yield json.loads(line)


def get_row(root: pathlib.Path, row_id: str) -> dict:
    paper, q = split_id(row_id)
    if not q:
        raise RowsError(f"{row_id!r} is a paper, not a leaf; add :<question>, e.g. {paper}:3(b)(ii)")
    for r in load_paper_rows(root, paper):
        if r["id"] == row_id:
            return r
    near = [r["id"] for r in load_paper_rows(root, paper) if r["id"].startswith(row_id)]
    hint = f"; leaves under it: {', '.join(near)}" if near else ""
    raise RowsError(f"{row_id} not found{hint}")


def paper_files(root: pathlib.Path, paper: str) -> dict[str, pathlib.Path]:
    inv = inventory(root)
    if paper not in inv:
        raise RowsError(f"{paper} not in corpus/inventory.csv")
    rec, pp = inv[paper], sources_dir() / "pastpapers"
    out = {}
    for key in ("qp", "ms", "in", "er", "gt", "sf"):
        if rec.get(key):
            out[key] = pp / rec[key]
    return out


def done_ids(root: pathlib.Path, component: int) -> set[str]:
    path = root / "ledger" / LEDGER_FILES[component]
    if not path.exists():
        return set()
    with path.open(encoding="utf-8-sig", newline="") as f:
        cells = [r.get("独立题目", "") + "；" + r.get("复测结果", "") for r in csv.DictReader(f)]
    return {tok for c in cells for tok in re.split(r"[；;\s]+", c) if ":" in tok}


def newest_first(row: dict) -> tuple:
    return (-row["year"], -SESSION_ORDER[row["session"]], row["variant"], row["qn"], row["q"])


# ------------------------------------------------------------------ commands

def print_row(r: dict, show_ms: bool) -> None:
    head = f"{r['id']}  ({short_ref(r['id'])})  [{r['marks']} mark{'s' if r['marks'] != 1 else ''}]"
    if r.get("command_word"):
        head += f"  {r['command_word']}"
    print(head)
    meta = [f"QP p.{r['qp_page']}"]
    if show_ms:
        meta.append(f"MS p.{r['ms_page']}")
    if r.get("has_figure"):
        meta.append("HAS FIGURE → render the page")
    if r.get("flags"):
        meta.append("flags: " + ", ".join(r["flags"]))
    if r.get("extension"):
        meta.append("2021 extension")
    if r.get("equivalent_of"):
        meta.append(f"same as {r['equivalent_of']}")
    if r.get("types"):
        meta.append("type: " + (r["types"].get("primary") or "—"))
    print("  " + " · ".join(meta))
    if r.get("stem_ctx"):
        print("  -- context --")
        print(textwrap.indent(r["stem_ctx"].rstrip(), "  "))
    print("  -- question --")
    print(textwrap.indent(r["stem"].rstrip(), "  "))
    if show_ms:
        print("  -- MS --")
        print(textwrap.indent(r["ms_text"].rstrip(), "  "))
        if r.get("ms_max"):
            print(f"  (max {r['ms_max']})")
        for mp in r.get("markpoints", []):
            print(f"  MP{mp['n']} [{mp['marks']}] {mp['text']}  {{{', '.join(mp['skills'])}}}")
        if r.get("er"):
            print("  -- examiner report (易错 only, not a scoring source) --")
            print(textwrap.indent(r["er"].rstrip(), "  "))


def cmd_get(args, root) -> int:
    r = get_row(root, args.row_id)
    if args.json:
        if not args.ms:
            r = {k: v for k, v in r.items() if k not in ("ms_text", "markpoints", "ms_max", "er", "ms_page")}
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print_row(r, args.ms)
    return 0


def cmd_files(args, root) -> int:
    paper, _ = split_id(args.ref)
    for key, path in paper_files(root, paper).items():
        status = "" if path.exists() else "   (missing!)"
        print(f"{key:3} {path}{status}")
        if key == "sf" and path.is_dir():
            for f in sorted(path.rglob("*")):
                if f.is_file() and not f.name.startswith("."):
                    print(f"      {f.relative_to(path)}")
    return 0


def cmd_render(args, root) -> int:
    try:
        import pymupdf
    except ImportError as e:
        raise RowsError("PyMuPDF missing: run with ~/.venvs/alevel-cs/bin/python") from e
    r = get_row(root, args.row_id)
    paper = r["paper"]
    kind = "ms" if args.ms else "qp"
    pdf = paper_files(root, paper).get(kind)
    if not pdf or not pdf.exists():
        raise RowsError(f"{kind.upper()} PDF for {paper} not found")
    first = r["ms_page"] if args.ms else r["qp_page"]
    out_dir = pathlib.Path(args.out) if args.out else root / "work" / "tmp" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = re.sub(r"[^0-9A-Za-z_]", "", r["id"].replace(":", "_"))
    doc = pymupdf.open(pdf)
    for page_no in range(first, min(first + args.pages, doc.page_count + 1)):
        target = out_dir / f"{stem}_{kind}_p{page_no}.png"
        doc[page_no - 1].get_pixmap(dpi=args.dpi).save(target)
        print(target)
    return 0


def cmd_drills(args, root) -> int:
    code = args.code
    m = re.match(r"^P([1-4])-", code)
    if not m:
        raise RowsError(f"not a type code: {code!r} (expected e.g. P2-FH-03)")
    comp = int(m.group(1))
    done = done_ids(root, comp)
    rows = [r for r in all_rows(root, comp) if (r.get("types") or {}).get("primary") == code]
    cross = [r for r in all_rows(root, comp) if code in (r.get("types") or {}).get("cross", [])]
    if not rows and not cross:
        print(f"No leaves tagged {code} yet (tagging tasks T24/T34 add `types`). Use the handbook's drill list.")
        return 0

    def show(r: dict) -> None:
        tags = []
        if r["id"] in done:
            tags.append("已做")
        if r.get("equivalent_of"):
            tags.append(f"重复 {short_ref(r['equivalent_of'])}")
        if (r["session"], r["year"]) in RESERVED_SESSIONS:
            tags.append("保留")
        if r.get("has_figure"):
            tags.append("图")
        if r.get("flags"):
            tags.append("flags:" + ",".join(r["flags"]))
        cw = f"  {r['command_word']}" if r.get("command_word") else ""
        print(f"  {short_ref(r['id']):<18} [{r['marks']}]{cw}" + (f"  ({'；'.join(tags)})" if tags else "")
              + f"    {r['id']}")

    verified = sorted((r for r in rows if not r.get("extension")), key=newest_first)
    ext = sorted((r for r in rows if r.get("extension")), key=newest_first)
    if not args.all:
        fresh = [r for r in verified if r["id"] not in done and not r.get("equivalent_of")
                 and (r["session"], r["year"]) not in RESERVED_SESSIONS]
        print(f"{code}: next unused verified leaf → " + (short_ref(fresh[0]["id"]) if fresh else "none left"))
    print(f"2022–2026 verified ({len(verified)}):")
    for r in verified:
        show(r)
    if ext:
        print(f"2021 extension ({len(ext)}), has MS, not counted in stats:")
        for r in ext:
            show(r)
    if cross and args.all:
        print(f"Also cross-tagged {code} ({len(cross)}):")
        for r in sorted(cross, key=newest_first):
            show(r)
    return 0


def cmd_find(args, root) -> int:
    comp = parse_paper(args.paper)["component"] if args.paper else None
    if args.type:
        comp = int(args.type[1])
    pattern = re.compile(args.grep, re.I) if args.grep else None
    n = 0
    for r in all_rows(root, comp):
        if args.paper and r["paper"] != args.paper:
            continue
        types = r.get("types") or {}
        if args.type and args.type != types.get("primary") and args.type not in types.get("cross", []):
            continue
        if args.skill and not any(args.skill in mp.get("skills", []) for mp in r.get("markpoints", [])):
            continue
        if pattern:
            hay = r["stem"] + "\n" + r.get("stem_ctx", "") + ("\n" + r["ms_text"] if args.ms else "")
            if not pattern.search(hay):
                continue
        n += 1
        stem = " ".join(r["stem"].split())
        print(f"{short_ref(r['id']):<18} [{r['marks']}] {types.get('primary') or '':<10} {stem[:90]}")
    print(f"({n} leaves)")
    return 0


def cmd_ex(args, root) -> int:
    hits = []
    for meta in sorted((root / "practice").rglob("meta.json")) if (root / "practice").is_dir() else []:
        data = json.loads(meta.read_text(encoding="utf-8"))
        rows = (data.get("source") or {}).get("rows", [])
        if args.row_id in rows or data.get("id") == args.row_id:
            hits.append(meta.parent.relative_to(root))
    if not hits:
        print(f"No practice folder covers {args.row_id}.")
        return 0
    for h in hits:
        print(f"{h}    →  make try EX={h}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", help="repo root (default: nearest folder with AGENTS.md)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("get", help="show one leaf (MS hidden unless --ms)")
    p.add_argument("row_id")
    p.add_argument("--ms", action="store_true", help="also print MS text, mark points and examiner report")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("files", help="source PDF paths for a paper")
    p.add_argument("ref", help="paper code or row id")
    p = sub.add_parser("render", help="render the leaf's QP (or MS) page(s) to PNG")
    p.add_argument("row_id")
    p.add_argument("--ms", action="store_true")
    p.add_argument("--pages", type=int, default=1, help="how many pages from the start page (default 1)")
    p.add_argument("--dpi", type=int, default=110)
    p.add_argument("--out", help="output folder (default work/tmp/figures)")
    p = sub.add_parser("drills", help="leaves of one type, newest first")
    p.add_argument("code")
    p.add_argument("--all", action="store_true", help="also list cross-tagged leaves")
    p = sub.add_parser("find", help="search leaves")
    p.add_argument("--paper")
    p.add_argument("--type")
    p.add_argument("--skill", help="mark-point skill tag")
    p.add_argument("--grep", help="regex over stem/context (and MS with --ms)")
    p.add_argument("--ms", action="store_true")
    p = sub.add_parser("ex", help="practice folders covering a leaf")
    p.add_argument("row_id")
    args = ap.parse_args(argv)
    try:
        root = find_root(args.root)
        return {"get": cmd_get, "files": cmd_files, "render": cmd_render, "drills": cmd_drills,
                "find": cmd_find, "ex": cmd_ex}[args.cmd](args, root)
    except RowsError as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
