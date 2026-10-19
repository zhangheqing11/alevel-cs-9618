#!/usr/bin/env python3
"""Compare the committed blind snapshot (blind/) with the T33 pilot (papers/p4/pilot_*).

Verifies blind/manifest.json hashes first, so the comparison is always against the untouched
blind result. Returns a dict used by report_p4.py; run directly to print the disagreements.
"""
import csv
import hashlib
import json

from workbench import HERE, ROOT, records, norm


def verify_blind():
    manifest = json.loads((HERE / "blind/manifest.json").read_text(encoding="utf-8"))
    for name, digest in manifest["files"].items():
        actual = hashlib.sha256((HERE / "blind" / name).read_bytes()).hexdigest()
        if actual != digest:
            raise ValueError(f"blind snapshot modified: {name}")


def load_pilot():
    tags = {}
    with (ROOT / "papers/p4/pilot_tags.csv").open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            tags[row["id"]] = {"primary": row["primary"],
                               "cross": [c for c in row["cross"].split(";") if c],
                               "confidence": row["confidence"], "note": row["note"]}
    points = {p["id"]: p for p in records(ROOT / "papers/p4/pilot_markpoints.jsonl")}
    return tags, points


def split_key(item):
    if item is None:
        return None
    return (item["ms_max"], tuple((norm(m["text"]), m["marks"]) for m in item["markpoints"]))


def compare(blind_dir=None):
    verify_blind()
    blind_dir = blind_dir or HERE / "blind"
    btags = {t["id"]: t for t in records(blind_dir / "p4_tags.jsonl")}
    bpoints = {p["id"]: p for p in records(blind_dir / "p4_markpoints.jsonl")}
    ptags, ppoints = load_pilot()
    ids = list(ptags)
    primary_diff = [r for r in ids if btags[r]["primary"] != ptags[r]["primary"]]
    cross_diff = [r for r in ids if sorted(btags[r]["cross"]) != sorted(ptags[r]["cross"])]
    split_ids = sorted(set(ppoints) | {r for r in ids if r in bpoints})
    split_diff = [r for r in split_ids if split_key(bpoints.get(r)) != split_key(ppoints.get(r))]
    # skill agreement on rows whose split agrees: per point Jaccard and exact-set matches
    exact = total = 0
    jacc = 0.0
    skill_rows = []
    for r in split_ids:
        if r in split_diff:
            continue
        for a, b in zip(bpoints[r]["markpoints"], ppoints[r]["markpoints"]):
            sa, sb = set(a["skills"]), set(b["skills"])
            total += 1
            exact += sa == sb
            jacc += len(sa & sb) / len(sa | sb)
            if sa != sb:
                skill_rows.append((r, a["n"], sorted(sa), sorted(sb)))
    return {
        "rows": len(ids), "primary_diff": primary_diff, "cross_diff": cross_diff,
        "split_rows": len(split_ids), "split_diff": split_diff,
        "skill_points": total, "skill_exact": exact, "skill_jaccard": jacc / total if total else 0,
        "skill_rows": skill_rows, "btags": btags, "ptags": ptags, "bpoints": bpoints, "ppoints": ppoints,
    }


def main():
    c = compare()
    n = c["rows"]
    print(f"primary agree {n - len(c['primary_diff'])}/{n}; cross agree {n - len(c['cross_diff'])}/{n}; "
          f"split agree {c['split_rows'] - len(c['split_diff'])}/{c['split_rows']}; "
          f"skills exact {c['skill_exact']}/{c['skill_points']} jaccard {c['skill_jaccard']:.2f}")
    for r in c["primary_diff"]:
        print("PRIMARY", r, "blind", c["btags"][r]["primary"], c["btags"][r]["cross"], "| pilot",
              c["ptags"][r]["primary"], c["ptags"][r]["cross"], "|", c["ptags"][r]["note"])
    for r in c["cross_diff"]:
        if r not in c["primary_diff"]:
            print("CROSS", r, "blind", c["btags"][r]["cross"], "| pilot", c["ptags"][r]["cross"], "|", c["ptags"][r]["note"])
    for r in c["split_diff"]:
        b, p = c["bpoints"].get(r), c["ppoints"].get(r)
        print("SPLIT", r)
        print("   blind", b and (b["ms_max"], [(m["text"], m["marks"]) for m in b["markpoints"]]))
        print("   pilot", p and (p["ms_max"], [(m["text"], m["marks"]) for m in p["markpoints"]]))


if __name__ == "__main__":
    main()
