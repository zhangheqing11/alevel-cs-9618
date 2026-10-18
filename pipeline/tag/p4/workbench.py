"""Shared helpers for T34: read P4 rows, find duplicate rows, cut MS checklists.

Never reads papers/p4/pilot_* (blind tagging).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

# D26 / D29 private-use glyph table (same as tools/check.py); P4 rows currently contain none.
PUA_MAP = {
    "\uf020": " ", "\uf02d": "\u2212", "\uf03c": "<", "\uf03e": ">", "\uf0fc": "\u2713",
    "\uf0b7": "\u2022", "\uf0a1": "\u25cb", "\uf0ac": "\u2190", "\uf0b1": "\u00b1", "\uf0b4": "\u00d7",
    "\uf09f": "\u2022", "\uf0df": "\u2190", "\uf050": "\u2713", "\uf0f0": "\u21e8", "\uf0a5": "\u221e",
}
PUA_TABLE = str.maketrans(PUA_MAP)


def norm(text):
    """D26/D29 glyph mapping plus whitespace compression; case and punctuation kept."""
    return " ".join(text.translate(PUA_TABLE).split())


def records(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def rows():
    return {r["id"]: r for p in sorted((ROOT / "corpus/rows/p4").glob("*.jsonl")) for r in records(p)}


def duplicates(data):
    """{row id: source id} for equivalent_of rows and D42 ③ rows identical to the same-season _41 row."""
    result = {}
    for rid, row in data.items():
        if row.get("equivalent_of"):
            result[rid] = row["equivalent_of"]
            continue
        base = row["paper"][:-1] + "1:" + row["q"]
        if base != rid and base in data and all(
                norm(row[k]) == norm(data[base][k]) for k in ("stem", "stem_ctx", "ms_text")):
            result[rid] = base
    return result


END_RE = re.compile(r"(?m)^\s*(?:e\.g\.?|E\.g\.?|eg\b|Example|Pseudocode|Java\b|VB\.?NET|VB\b|Python\b|Sample)")
HEADER_RE = re.compile(r"(?im)^\s*(?:\d+|one) marks?\s+(?:each|per)\b.*$|^\s*(?:\d+|one) marks? for\s*:?\s*$")


def checklist_region(ms):
    text = ms.translate(PUA_TABLE)
    m = END_RE.search(text)
    return text[:m.start()] if m else text


def auto_items(ms):
    """Candidate markpoint texts: bullets of the language-neutral checklist."""
    region = checklist_region(ms)
    if "•" in region:
        parts = region.split("•")[1:]
        items = []
        for part in parts:
            # drop a following section header ("1 mark each to max 6") that leaks into the bullet
            lines = part.split("\n")
            keep = [lines[0]]
            for line in lines[1:]:
                if HEADER_RE.match(line):
                    break
                keep.append(line)
            items.append(norm("\n".join(keep)))
        return [i for i in items if i]
    lines = [norm(l) for l in region.split("\n") if l.strip()]
    found = [l for l in lines if re.match(r"(?i)(?:\d+|one) marks? (?:for|per) ", l)]
    return found


if __name__ == "__main__":
    data = rows()
    dups = duplicates(data)
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    for rid, r in data.items():
        if rid in dups or r["paper"] != sys.argv[1]:
            continue
        print(f"\n=== {r['q']} [{r['marks']}{' FIG' if r['has_figure'] else ''}]")
        stem = re.sub(r"\.{3,}", "", norm(r["stem"]))
        stem = re.sub(r"Save your program.*?evidence document\.", "", stem)
        stem = re.sub(r"Copy and paste the program code into part .*? in the evidence document\.", "", stem)
        print("Q:", stem[:limit])
        region = norm(checklist_region(r["ms_text"]))
        print("MS:", region[:1200])
        if r["marks"] >= 2:
            for n, item in enumerate(auto_items(r["ms_text"]), 1):
                print(f"  {n}. {item}")
