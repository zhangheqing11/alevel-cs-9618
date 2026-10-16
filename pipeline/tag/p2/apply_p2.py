#!/usr/bin/env python3
"""Merge only T28-owned annotations, preserving all other row bytes verbatim."""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OWNED = ("types", "tag_confidence", "tag_note", "markpoints", "ms_max")


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def annotated_line(line, tags, points):
    row = json.loads(line)
    rid = row["id"]
    tag = tags[rid]
    additions = {"types": {"primary": tag["primary"], "cross": tag["cross"]},
                 "tag_confidence": tag["confidence"], "tag_note": tag["note"]}
    if rid in points:
        additions["markpoints"] = points[rid]["markpoints"]
        if points[rid]["ms_max"] is not None:
            additions["ms_max"] = points[rid]["ms_max"]
    # Existing source lines use flat top-level JSON. Find value spans with a JSON
    # decoder rather than reserialising unrelated keys or changing their escapes.
    decoder = json.JSONDecoder()
    spans = []
    position = line.index("{") + 1
    while True:
        while line[position].isspace() or line[position] == ",":
            position += 1
        if line[position] == "}":
            break
        start = position
        key, position = decoder.raw_decode(line, position)
        while line[position].isspace() or line[position] == ":":
            position += 1
        _, end = decoder.raw_decode(line, position)
        spans.append((key, start, end))
        position = end
    base_parts = [line[start:end] for key, start, end in spans if key not in OWNED]
    for key, value in additions.items():
        base_parts.append(json.dumps(key) + ": " + json.dumps(value, ensure_ascii=False))
    return "{" + ", ".join(base_parts) + "}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check whether the merge is current without writing")
    args = parser.parse_args()
    tags = {row["id"]: row for row in read_jsonl(HERE / "p2_tags.jsonl")}
    points = {row["id"]: row for row in read_jsonl(HERE / "p2_markpoints.jsonl")}
    row_ids = {row["id"] for path in (ROOT / "corpus/rows/p2").glob("*.jsonl") for row in read_jsonl(path)}
    if set(tags) != row_ids or not set(points) <= row_ids:
        raise ValueError("annotation ids must cover precisely the P2 corpus")
    changed = []
    for path in sorted((ROOT / "corpus/rows/p2").glob("*.jsonl")):
        before = path.read_text(encoding="utf-8")
        after = "\n".join(annotated_line(line, tags, points) for line in before.splitlines()) + "\n"
        if before != after:
            changed.append(path.name)
            if not args.check:
                path.write_text(after, encoding="utf-8")
    if args.check and changed:
        raise SystemExit("stale merged files: " + ", ".join(changed))
    print(f"{len(tags)} P2 rows; {len(points)} markpoint sets; {len(changed)} changed files")


if __name__ == "__main__":
    main()
