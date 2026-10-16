#!/usr/bin/env python3
"""Repository validator: `make check` (changed exercises only) / `make check-all`.

Checks, each skipped silently when its inputs do not exist yet:
  inventory   corpus/inventory.csv header
  rows        corpus/rows/p<N>/<paper>.jsonl schema, ids, mark totals
  taxonomy    papers/p<N>/taxonomy.json schema, codes; rows' types exist
  skill tags  papers/p<N>/skill_tags.json schema; markpoint skills exist
  cards       ⟦row id⟧ references and 「MS quote」⟦row id⟧ exact-quote audit;
              type-card headings use taxonomy codes
  exercises   meta.json schema, required files, ref passes, every mutant fails
  ledger      ledger/*.csv header
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import pathlib
import re
import subprocess
import sys
import unicodedata

import jsonschema

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
PY = sys.executable

INVENTORY_COLS = ["paper", "component", "session", "year", "variant", "corpus", "qp", "ms", "in", "sf",
                  "er", "gt", "total_marks", "qp_sha256", "ms_sha256", "duplicate_of", "status"]
LEDGER_COLS = ["类型", "名称", "章节", "优先级", "状态", "日期", "独立题目", "得分", "错误类别", "失分技能",
               "解释证据", "复测日期", "复测结果"]
ROW_REF = re.compile(r"⟦(9618_[msw]\d{2}_[1-4][1-3]:[^⟧\s]+)⟧")
QUOTE_REF = re.compile(r"「([^」]+)」\s*⟦(9618_[msw]\d{2}_[1-4][1-3]:[^⟧\s]+)⟧")
CARD_HEADING = re.compile(r"^###\s+(P[1-4]-[A-Z]{2,3}-\d{2})\s")
PAPER_RE = re.compile(r"^9618_[msw]\d{2}_([1-4])[1-3]$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notes: list[str] = []

    def err(self, where, msg: str) -> None:
        self.errors.append(f"{rel(where)}: {msg}")

    def note(self, msg: str) -> None:
        self.notes.append(msg)


def rel(p) -> str:
    try:
        return str(pathlib.Path(p).resolve().relative_to(ROOT))
    except (ValueError, TypeError):
        return str(p)


def schema(name: str) -> jsonschema.Draft202012Validator:
    return jsonschema.Draft202012Validator(json.loads((SCHEMAS / name).read_text(encoding="utf-8")))


def schema_errors(validator, obj) -> list[str]:
    return [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}"
            for e in sorted(validator.iter_errors(obj), key=lambda e: list(map(str, e.absolute_path)))]


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    text = text.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    text = text.replace("←", "<-").replace("–", "-").replace("—", "-")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r" ?/ ?", "/", text)  # MS writes "field / attribute" and "field/attribute" interchangeably
    return text.strip(" .;,:")


# ---------------------------------------------------------------- inventory

def load_inventory(rep: Report) -> dict[str, dict]:
    path = ROOT / "corpus" / "inventory.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = [c for c in INVENTORY_COLS if c not in (reader.fieldnames or [])]
        if missing:
            rep.err(path, f"missing columns {missing}")
            return {}
        rows = list(reader)
    inv = {}
    for r in rows:
        if not PAPER_RE.match(r["paper"]):
            rep.err(path, f"bad paper id {r['paper']!r}")
        if r["paper"] in inv:
            rep.err(path, f"duplicate paper {r['paper']}")
        inv[r["paper"]] = r
    rep.note(f"inventory: {len(inv)} papers")
    return inv


# --------------------------------------------------------------------- rows

def load_rows(rep: Report, inventory: dict) -> dict[str, dict]:
    rows_dir = ROOT / "corpus" / "rows"
    if not rows_dir.exists():
        return {}
    validator = schema("row.schema.json")
    all_rows: dict[str, dict] = {}
    n_files = 0
    for path in sorted(rows_dir.glob("p[1-4]/*.jsonl")):
        n_files += 1
        paper = path.stem
        m = PAPER_RE.match(paper)
        if not m:
            rep.err(path, "file name must be <paper>.jsonl")
            continue
        if path.parent.name != f"p{m.group(1)}":
            rep.err(path, f"paper {paper} filed under {path.parent.name}")
        total = 0
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                rep.err(path, f"line {i}: invalid JSON ({e})")
                continue
            for e in schema_errors(validator, row):
                rep.err(path, f"line {i}: {e}")
            rid = row.get("id", f"<line {i}>")
            if row.get("paper") != paper or not str(rid).startswith(paper + ":"):
                rep.err(path, f"line {i}: id/paper {rid!r} does not match file")
            if rid in all_rows:
                rep.err(path, f"duplicate row id {rid}")
            all_rows[rid] = row
            total += row.get("marks", 0) if isinstance(row.get("marks"), int) else 0
            if not str(row.get("ms_text", "")).strip() and "ms-misaligned" not in row.get("flags", []):
                rep.err(path, f"{rid}: empty ms_text (flag ms-misaligned if genuinely unresolved)")
        inv = inventory.get(paper)
        if inv is None:
            if inventory:
                rep.err(path, f"paper {paper} not in corpus/inventory.csv")
        elif inv.get("total_marks", "").strip():
            expected = int(inv["total_marks"])
            if total != expected:
                rep.err(path, f"marks sum {total} != total_marks {expected}")
    if n_files:
        rep.note(f"rows: {len(all_rows)} leaves in {n_files} papers")
    return all_rows


# ----------------------------------------------------------- taxonomy, tags

def load_taxonomies(rep: Report) -> dict[str, dict]:
    validator = schema("taxonomy.schema.json")
    types: dict[str, dict] = {}
    for path in sorted((ROOT / "papers").glob("p[1-4]/taxonomy.json")):
        comp = int(path.parent.name[1])
        try:
            tax = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            rep.err(path, f"invalid JSON ({e})")
            continue
        for e in schema_errors(validator, tax):
            rep.err(path, e)
        if tax.get("component") != comp:
            rep.err(path, f"component {tax.get('component')} != directory p{comp}")
        chapters = {c.get("code") for c in tax.get("chapters", [])}
        for t in tax.get("types", []):
            code = t.get("code", "")
            if not code.startswith(f"P{comp}-"):
                rep.err(path, f"type {code} must start with P{comp}-")
            if t.get("chapter") not in chapters:
                rep.err(path, f"type {code}: unknown chapter {t.get('chapter')}")
            if code.split("-")[1:2] != [t.get("chapter")]:
                rep.err(path, f"type {code}: code chapter part != chapter {t.get('chapter')}")
            if code in types:
                rep.err(path, f"duplicate type code {code}")
            types[code] = t
    if types:
        rep.note(f"taxonomy: {len(types)} types")
    return types


def load_skill_tags(rep: Report) -> dict[int, set[str]]:
    validator = schema("skill_tags.schema.json")
    vocab: dict[int, set[str]] = {}
    raw: dict[int, dict] = {}
    for path in sorted((ROOT / "papers").glob("p[1-4]/skill_tags.json")):
        comp = int(path.parent.name[1])
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            rep.err(path, f"invalid JSON ({e})")
            continue
        for e in schema_errors(validator, data):
            rep.err(path, e)
        tags = [t.get("tag") for t in data.get("tags", [])]
        if len(tags) != len(set(tags)):
            rep.err(path, "duplicate tags")
        raw[comp] = data
        vocab[comp] = set(tags)
    for comp, data in raw.items():
        ext = data.get("extends")
        if ext:
            m = re.search(r"p([1-4])/skill_tags\.json$", ext)
            if m and int(m.group(1)) in vocab:
                vocab[comp] |= vocab[int(m.group(1))]
            else:
                rep.err(ROOT / "papers" / f"p{comp}" / "skill_tags.json", f"extends unknown vocabulary {ext}")
    return vocab


def check_row_links(rep: Report, rows: dict, types: dict, vocab: dict) -> None:
    for rid, row in rows.items():
        t = row.get("types")
        if t:
            for code in [t.get("primary")] + list(t.get("cross", [])):
                if code and code not in types:
                    rep.err(f"corpus/rows ({rid})", f"unknown type code {code}")
        for mp in row.get("markpoints", []) or []:
            comp = row.get("component")
            for s in mp.get("skills", []):
                if comp not in vocab:
                    rep.err(f"corpus/rows ({rid})", f"markpoint skill {s} but papers/p{comp}/skill_tags.json missing")
                    break
                if s not in vocab[comp]:
                    rep.err(f"corpus/rows ({rid})", f"unknown skill tag {s}")


# -------------------------------------------------------------------- cards

def check_markdown(rep: Report, rows: dict, types: dict) -> None:
    md_files = [p for base in ("papers", "ladder", "skill") for p in sorted((ROOT / base).rglob("*.md"))]
    n_refs = n_quotes = 0
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            m = CARD_HEADING.match(line)
            if m and "papers" in path.parts and m.group(1) not in types:
                rep.err(path, f"line {lineno}: card heading uses unknown type {m.group(1)}")
        for m in ROW_REF.finditer(text):
            n_refs += 1
            if m.group(1) not in rows:
                line = text.count("\n", 0, m.start()) + 1
                rep.err(path, f"line {line}: reference to unknown row {m.group(1)}")
        for m in QUOTE_REF.finditer(text):
            n_quotes += 1
            quote, rid = m.group(1), m.group(2)
            row = rows.get(rid)
            if row is None:
                continue  # already reported above
            if norm(quote) not in norm(row.get("ms_text", "")):
                line = text.count("\n", 0, m.start()) + 1
                rep.err(path, f"line {line}: quote not found verbatim in MS of {rid}: 「{quote[:60]}」")
    if n_refs:
        rep.note(f"markdown: {n_refs} row refs, {n_quotes} MS quotes audited in {len(md_files)} files")


# ---------------------------------------------------------------- exercises

def changed_paths() -> set[str] | None:
    """Files changed vs the merge-base with origin/main (or main), plus uncommitted. None = unknown."""
    def git(*args):
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    base = None
    for ref in ("origin/main", "main"):
        r = git("merge-base", ref, "HEAD")
        if r.returncode == 0:
            base = r.stdout.strip()
            break
    if base is None:
        return None
    out = set(git("diff", "--name-only", base, "HEAD").stdout.split("\n"))
    for line in git("status", "--porcelain", "--untracked-files=all").stdout.splitlines():
        out.add(line[3:].strip().strip('"'))
    return {p for p in out if p}


def run_pytest(test_file: pathlib.Path, candidate: pathlib.Path) -> tuple[int, str]:
    env = dict(os.environ, CANDIDATE=str(candidate), PYTHONDONTWRITEBYTECODE="1")
    proc = subprocess.run(
        [PY, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", str(ROOT), str(test_file)],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=120,
    )
    return proc.returncode, proc.stdout + proc.stderr


def check_exercises(rep: Report, rows: dict, types: dict, vocab: dict, all_exercises: bool, only: str | None) -> None:
    validator = schema("exercise.schema.json")
    metas = sorted(p for base in ("practice", "ladder", "schemas/examples")
                   for p in (ROOT / base).rglob("meta.json") if "attempts" not in p.parts)
    changed = None if all_exercises else changed_paths()
    ran = 0
    for meta_path in metas:
        ex = meta_path.parent
        ex_rel = rel(ex)
        if only and not ex_rel.startswith(only.rstrip("/")):
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            rep.err(meta_path, f"invalid JSON ({e})")
            continue
        for e in schema_errors(validator, meta):
            rep.err(meta_path, e)
        required = ["task.md", "starter.py", "test_task.py", "ref/solution.py"]
        if meta.get("pseudocode"):
            required.append("answer.pseudo")
        for f in required:
            if not (ex / f).exists():
                rep.err(ex, f"missing {f}")
        for f in meta.get("files", []):
            if not (ex / "files" / f).exists():
                rep.err(ex, f"meta.files lists {f} but files/{f} is missing")
        mutants = sorted((ex / "ref").glob("mutant_*.py"))
        if not mutants:
            rep.err(ex, "needs at least one ref/mutant_*.py")
        src = meta.get("source")
        if src and rows:
            for rid in src.get("rows", []):
                if rid not in rows:
                    rep.err(meta_path, f"source row {rid} not in corpus")
        if types:
            for code in meta.get("types", []):
                if code not in types:
                    rep.err(meta_path, f"unknown type code {code}")
        all_tags = set().union(*vocab.values()) if vocab else set()
        if all_tags and "schemas" not in ex.parts:  # D8: one shared skill vocabulary
            for s in meta.get("skills", []):
                if s not in all_tags:
                    rep.err(meta_path, f"skill tag {s} not in papers/p*/skill_tags.json")
        # Run tests only when the exercise changed (or --all / --only)
        if not (all_exercises or only) and changed is not None:
            if not any(p.startswith(ex_rel + "/") for p in changed):
                continue
        test_file, ref = ex / "test_task.py", ex / "ref" / "solution.py"
        if not (test_file.exists() and ref.exists()):
            continue
        ran += 1
        rc, out = run_pytest(test_file, ref)
        if rc != 0 or " passed" not in out:
            tail = "\n      ".join(out.strip().splitlines()[-8:])
            rep.err(ex, f"reference solution does not pass all tests:\n      {tail}")
        for mutant in mutants:
            rc, out = run_pytest(test_file, mutant)
            if rc != 1:
                why = "passes every test" if rc == 0 else f"pytest exit {rc} (error, not a test failure)"
                rep.err(ex, f"{mutant.name} must fail at least one test but {why}")
    if metas:
        rep.note(f"exercises: {len(metas)} found, {ran} executed"
                 + ("" if all_exercises or only else " (changed only; `make check-all` runs all)"))


# ------------------------------------------------------------------- ledger

def check_ledger(rep: Report) -> None:
    for path in sorted((ROOT / "ledger").glob("*.csv")):
        with path.open(encoding="utf-8-sig", newline="") as f:
            header = next(csv.reader(f), [])
        if header != LEDGER_COLS:
            rep.err(path, f"header must be {LEDGER_COLS}")


# --------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all-exercises", action="store_true", help="run every exercise, not only changed ones")
    ap.add_argument("--only", help="limit exercise runs to this path prefix")
    ap.add_argument("--no-exercises", action="store_true")
    args = ap.parse_args()

    rep = Report()
    inventory = load_inventory(rep)
    rows = load_rows(rep, inventory)
    types = load_taxonomies(rep)
    vocab = load_skill_tags(rep)
    check_row_links(rep, rows, types, vocab)
    check_markdown(rep, rows, types)
    if not args.no_exercises:
        check_exercises(rep, rows, types, vocab, args.all_exercises, args.only)
    check_ledger(rep)

    for n in rep.notes:
        print(f"  · {n}")
    if rep.errors:
        print(f"\n✗ make check: {len(rep.errors)} problem(s)")
        for e in rep.errors:
            print(f"  - {e}")
        return 1
    print("✓ make check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
