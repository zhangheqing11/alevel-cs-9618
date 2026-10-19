#!/usr/bin/env python3
"""Merge T34-owned annotations into corpus/rows/p4/*.jsonl, keeping every other byte verbatim.

Owns only types, tag_confidence, tag_note, markpoints, ms_max. Other fields (er, equivalent_of, ...)
keep their original text, order and escapes (D33). Re-runnable; --check writes nothing and exits 1
when a file would change.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ROWS = ROOT / "corpus/rows/p4"
OWNED = ("types", "tag_confidence", "tag_note", "markpoints", "ms_max")
DECODER = json.JSONDecoder()


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def index_records(records):
    result = {}
    for item in records:
        if item["id"] in result:
            raise ValueError("duplicate annotation id: " + item["id"])
        result[item["id"]] = item
    return result


def top_level_spans(line):
    """[(key, start, end)] covering '"key":value' for each top-level member, and the index of '}'."""
    spans = []
    pos = line.index("{") + 1
    while True:
        while line[pos].isspace() or line[pos] == ",":
            pos += 1
        if line[pos] == "}":
            return spans, pos
        start = pos
        key, pos = DECODER.raw_decode(line, pos)
        while line[pos].isspace() or line[pos] == ":":
            pos += 1
        _, end = DECODER.raw_decode(line, pos)
        spans.append((key, start, end))
        pos = end


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def annotated_line(line, tags, points):
    rid = json.loads(line)["id"]
    tag = tags[rid]
    additions = {"types": {"primary": tag["primary"], "cross": tag["cross"]},
                 "tag_confidence": tag["confidence"], "tag_note": tag["note"]}
    if rid in points:
        additions["markpoints"] = points[rid]["markpoints"]
        if points[rid]["ms_max"] is not None:
            additions["ms_max"] = points[rid]["ms_max"]
    spans, close = top_level_spans(line)
    kept = [line[s:e] for key, s, e in spans if key not in OWNED]
    # separator between members as used in the original line (P4 rows are compact: ",")
    sep = ","
    if len(spans) >= 2:
        between = line[spans[0][2]:spans[1][1]]
        sep = between if between.strip() == "," else ","
    parts = kept + [encode(k) + ":" + encode(v) for k, v in additions.items()]
    return line[:line.index("{") + 1] + sep.join(parts) + line[close:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale files without writing")
    args = parser.parse_args()
    tags = index_records(read_jsonl(HERE / "p4_tags.jsonl"))
    points = index_records(read_jsonl(HERE / "p4_markpoints.jsonl"))
    row_ids = {row["id"] for path in ROWS.glob("*.jsonl") for row in read_jsonl(path)}
    if set(tags) != row_ids or not set(points) <= row_ids:
        raise ValueError("annotation ids must cover precisely the P4 corpus")
    changed = []
    for path in sorted(ROWS.glob("*.jsonl")):
        before = path.read_text(encoding="utf-8")
        lines = before.splitlines()
        after = "\n".join(annotated_line(l, tags, points) if l.strip() else l for l in lines)
        if before.endswith("\n"):
            after += "\n"
        if before != after:
            changed.append(path.name)
            if not args.check:
                path.write_text(after, encoding="utf-8")
    if args.check and changed:
        raise SystemExit("stale merged files: " + ", ".join(changed))
    print(f"{len(tags)} P4 rows; {len(points)} markpoint sets; {len(changed)} changed files")


if __name__ == "__main__":
    main()
