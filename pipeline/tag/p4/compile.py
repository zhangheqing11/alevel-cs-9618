#!/usr/bin/env python3
"""Compile the hand-written spec files (spec/<paper>.txt) into p4_tags.jsonl and p4_markpoints.jsonl.

Spec format, one block per independent row (duplicates are copied from their source row):

    1(b) LT-01 +AR-03 low # free-text note
     = skill,skill | skill | ...        skills for each markpoint, in order
     w 4,1,1                            optional weights (default 1 each)
     t text || text || ...              optional explicit markpoint texts (default: MS checklist bullets)
     nolist                             marks >= 2 but MS has no checklist: no split, standard note

The header gives the q label, the primary type (without "P4-"), cross types prefixed "+",
"low" for low confidence, and an optional note after "#". Never reads papers/p4/pilot_*.
"""
import json
import sys
from copy import deepcopy

from workbench import HERE, rows, duplicates, norm, auto_items

NOLIST_NOTE = "MS 无计分清单，未拆"


def parse_spec(path, paper):
    blocks = {}
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("//"):
            continue
        if not raw[0].isspace():
            head, _, note = raw.partition("#")
            tokens = head.split()
            q, primary = tokens[0], tokens[1]
            current = {"q": q, "primary": "P4-" + primary, "cross": [], "low": False,
                       "note": note.strip(), "skills": None, "weights": None, "texts": None, "nolist": False}
            for tok in tokens[2:]:
                if tok.startswith("+"):
                    current["cross"].append("P4-" + tok[1:])
                elif tok == "low":
                    current["low"] = True
                else:
                    raise ValueError(f"{paper} {q}: bad token {tok}")
            rid = f"{paper}:{q}"
            if rid in blocks:
                raise ValueError(f"duplicate spec {rid}")
            blocks[rid] = current
            continue
        line = raw.strip()
        if line.startswith("="):
            current["skills"] = [[s.strip() for s in grp.split(",") if s.strip()] for grp in line[1:].split("|")]
        elif line.startswith("w "):
            current["weights"] = [int(x) for x in line[2:].split(",")]
        elif line.startswith("t "):
            current["texts"] = [t.strip() for t in line[2:].split("||")]
        elif line == "nolist":
            current["nolist"] = True
        else:
            raise ValueError(f"{paper} {current['q']}: bad line {line!r}")
    return blocks


def compile_all(spec_dir=None):
    spec_dir = spec_dir or HERE / "spec"
    data = rows()
    dups = duplicates(data)
    specs = {}
    for path in sorted(spec_dir.glob("*.txt")):
        specs.update(parse_spec(path, path.stem))
    tags, points = {}, {}
    for rid, spec in specs.items():
        if rid not in data:
            raise ValueError(f"spec for unknown row {rid}")
        if rid in dups:
            raise ValueError(f"spec for duplicate row {rid} (copied from {dups[rid]})")
        row = data[rid]
        note = spec["note"]
        if spec["nolist"]:
            note = (note + "；" if note else "") + NOLIST_NOTE
        tags[rid] = {"id": rid, "primary": spec["primary"], "cross": spec["cross"],
                     "confidence": "low" if spec["low"] else "high", "note": note}
        if row["marks"] < 2 or spec["nolist"]:
            if spec["skills"] is not None:
                raise ValueError(f"{rid}: skills given for a row that is not split")
            continue
        texts = spec["texts"] or auto_items(row["ms_text"])
        if spec["skills"] is None:
            raise ValueError(f"{rid}: split row needs skills ({len(texts)} items)")
        if len(texts) != len(spec["skills"]):
            raise ValueError(f"{rid}: {len(texts)} texts but {len(spec['skills'])} skill groups")
        weights = spec["weights"] or [1] * len(texts)
        if len(weights) != len(texts):
            raise ValueError(f"{rid}: weights length")
        mps = []
        for n, (text, skills, marks) in enumerate(zip(texts, spec["skills"], weights), 1):
            if norm(text) not in norm(row["ms_text"]):
                raise ValueError(f"{rid}: text not in MS: {text!r}")
            mps.append({"n": n, "text": text, "marks": marks, "skills": skills})
        total = sum(weights)
        if total < row["marks"]:
            raise ValueError(f"{rid}: markpoints total {total} < marks {row['marks']}")
        points[rid] = {"id": rid, "ms_max": row["marks"] if total > row["marks"] else None, "markpoints": mps}
    # copy duplicates (D42 ③, guide §6)
    for rid, src in dups.items():
        if src not in tags:
            continue
        t = deepcopy(tags[src]); t["id"] = rid; tags[rid] = t
        if src in points:
            p = deepcopy(points[src]); p["id"] = rid; points[rid] = p
    order = list(data)
    return ([tags[r] for r in order if r in tags], [points[r] for r in order if r in points], data)


def dump(path, items):
    path.write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items), encoding="utf-8")


def main():
    tags, points, data = compile_all()
    missing = [r for r in data if r not in {t["id"] for t in tags}]
    dump(HERE / "p4_tags.jsonl", tags)
    dump(HERE / "p4_markpoints.jsonl", points)
    print(f"{len(tags)}/{len(data)} tagged; {len(points)} split rows; "
          f"{sum(len(p['markpoints']) for p in points)} points; {len(missing)} untagged")
    if "-v" in sys.argv and missing:
        print("untagged:", " ".join(missing[:40]))


if __name__ == "__main__":
    main()
