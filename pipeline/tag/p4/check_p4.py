#!/usr/bin/env python3
"""Validate the P4 annotation sources (p4_tags.jsonl, p4_markpoints.jsonl). Never reads pilot inputs."""
import json

from workbench import HERE, ROOT, rows, records, duplicates, norm

NOLIST_NOTE = "MS 无计分清单，未拆"
FORBIDDEN = {"flowchart-draw", "flowchart-to-pseudocode", "trace-dry-run", "case-of", "case-range",
             "random-file", "user-defined-type"}  # guide §8.3


def require(condition, message):
    if not condition:
        raise ValueError(message)


def index(items):
    result = {}
    for item in items:
        require(item["id"] not in result, "duplicate id " + item["id"])
        result[item["id"]] = item
    return result


def load_skills(path):
    vocabulary = json.loads(path.read_text(encoding="utf-8"))
    result = {item["tag"] for item in vocabulary["tags"]}
    if vocabulary.get("extends"):
        result |= load_skills(ROOT / vocabulary["extends"])
    return result


def validate(data, tags, points, inherited, type_codes, skills):
    require(set(tags) == set(data), "tag coverage must equal corpus ids")
    must_split = {rid for rid, row in data.items() if row["marks"] >= 2
                  and NOLIST_NOTE not in tags[rid]["note"]}
    require(set(points) == must_split, "split rows must be exactly the >= 2 mark rows with a checklist "
            f"(missing {sorted(must_split - set(points))[:5]}, extra {sorted(set(points) - must_split)[:5]})")
    for rid, tag in tags.items():
        require(set(tag) == {"id", "primary", "cross", "confidence", "note"}, f"{rid}: tag fields")
        require(tag["primary"] in type_codes and set(tag["cross"]) <= type_codes, f"{rid}: type code")
        require(len(set(tag["cross"])) == len(tag["cross"]) <= 2 and tag["primary"] not in tag["cross"],
                f"{rid}: cross types")
        require(tag["confidence"] in {"high", "low"} and (tag["confidence"] != "low" or bool(tag["note"])),
                f"{rid}: confidence/note")
    for rid, item in points.items():
        require(set(item) == {"id", "ms_max", "markpoints"} and item["markpoints"], f"{rid}: point set")
        total = 0
        for n, point in enumerate(item["markpoints"], 1):
            require(set(point) == {"n", "text", "marks", "skills"} and point["n"] == n, f"{rid}: point fields")
            require(bool(point["text"]) and norm(point["text"]) in norm(data[rid]["ms_text"]),
                    f"{rid}: non-verbatim text {point['text']!r}")
            require(type(point["marks"]) is int and point["marks"] >= 1, f"{rid}: point marks")
            sk = point["skills"]
            require(1 <= len(sk) <= 3 and len(set(sk)) == len(sk) and set(sk) <= skills and not set(sk) & FORBIDDEN,
                    f"{rid}: invalid skills {sk}")
            total += point["marks"]
        cap = item["ms_max"]
        require((cap is None and total == data[rid]["marks"]) or (cap == data[rid]["marks"] and total > cap),
                f"{rid}: point total {total} / ms_max {cap} / marks {data[rid]['marks']}")
    for rid, parent in inherited.items():
        strip = lambda d: {k: v for k, v in d.items() if k != "id"}
        require(strip(tags[rid]) == strip(tags[parent]), f"{rid}: inherited tags differ from {parent}")
        require((rid in points) == (parent in points), f"{rid}: inherited split missing")
        if rid in points:
            require(strip(points[rid]) == strip(points[parent]), f"{rid}: inherited points differ")


def main():
    data = rows()
    tags = index(records(HERE / "p4_tags.jsonl"))
    points = index(records(HERE / "p4_markpoints.jsonl"))
    types = {t["code"] for t in json.loads((ROOT / "papers/p4/taxonomy.json").read_text(encoding="utf-8"))["types"]}
    validate(data, tags, points, duplicates(data), types, load_skills(ROOT / "papers/p4/skill_tags.json"))
    require(len(data) == 744, "expected 744 P4 rows")
    low = sum(t["confidence"] == "low" for t in tags.values())
    require(low < 0.1 * len(data), "low confidence exceeds 10%")
    print(f"{len(tags)}/{len(data)} tags; {len(points)} split rows; "
          f"{sum(len(p['markpoints']) for p in points.values())} points; {low} low; validation passed")


if __name__ == "__main__":
    main()
