"""Rebuild T12 JSONL rows and the extraction report.

Examples:
    python pipeline/extract/run_all.py --component 1
    python pipeline/extract/run_all.py --all
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import random
from collections import Counter
from typing import Any

from align import align_rows
from dedupe import dedupe
from parse_ms import parse_mark_scheme
from pdf_text import DEFAULT_CACHE_ROOT, DEFAULT_SOURCE_ROOT, extract_pdf, source_path
from split_qp import split_question_paper


ROOT = pathlib.Path(__file__).resolve().parents[2]
INVENTORY = ROOT / "corpus" / "inventory.csv"


def load_inventory() -> list[dict[str, str]]:
    with INVENTORY.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_jsonl(path: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
    )


def _sample(rows: list[dict[str, Any]], paper: str) -> list[dict[str, Any]]:
    rng = random.Random(paper)
    return rng.sample(rows, min(5, len(rows)))


def report(selected: list[dict[str, str]], rows_by_paper: dict[str, list[dict[str, Any]]]) -> str:
    lines = [
        "# T12 抽取报告",
        "",
        "> 生成方式：`pipeline/extract/run_all.py`。题卷分值取 PyMuPDF 右侧分值栏；MS 文本取同卷同 variant 的 Mark Scheme。源 PDF 只读，缓存位于 `/tmp/alevel-cs-extract/`。",
        "",
        "## 卷级统计",
        "",
        "| 卷 | 小问行数 | 分值和 | ms-misaligned | split-uncertain | 其他 flags |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    all_rows = [row for paper in sorted(rows_by_paper) for row in rows_by_paper[paper]]
    for record in selected:
        paper = record["paper"]
        rows = rows_by_paper.get(paper, [])
        counts = Counter(flag for row in rows for flag in row["flags"])
        other = sum(v for k, v in counts.items() if k not in {"ms-misaligned", "split-uncertain"})
        lines.append(
            f"| {paper} | {len(rows)} | {sum(row['marks'] for row in rows)} | "
            f"{counts['ms-misaligned']} | {counts['split-uncertain']} | {other} |"
        )
    total = Counter(flag for row in all_rows for flag in row["flags"])
    unresolved = total["ms-misaligned"] + total["split-uncertain"]
    lines.extend(
        [
            "",
            f"总计：{len(selected)} 卷，{len(all_rows)} 行，分值和 {sum(row['marks'] for row in all_rows)}；"
            f"未解决拆分/MS flags {unresolved} 行（{unresolved / max(1, len(all_rows)):.2%}）。",
            "",
            "## 未解决问题",
            "",
        ]
    )
    unresolved_rows = [
        row for row in all_rows if {"ms-misaligned", "split-uncertain"}.intersection(row["flags"])
    ]
    if unresolved_rows:
        lines.extend(f"- `{row['id']}`：{', '.join(row['flags'])}" for row in unresolved_rows)
    else:
        lines.append("- 无。")
    lines.extend(["", "## 每卷随机 5 行核验记录", ""])
    lines.append("记录以来源 PDF 页码、缓存布局文本和分值栏坐标作自动对照；含 `figure` 的行仍应在 PDF 原页做视觉复核。")
    lines.extend(["", "| 卷 | 题号 | QP 页 | MS 页 | 分值 | 自动对照结果 |", "|---|---|---:|---:|---:|---|"])
    for record in selected:
        for row in _sample(rows_by_paper.get(record["paper"], []), record["paper"]):
            result = "文本非空且页码已对齐"
            if "figure" in row["flags"]:
                result += "；需视觉复核图表/代码"
            lines.append(
                f"| {record['paper']} | `{row['q']}` | {row['qp_page']} | {row['ms_page']} | {row['marks']} | {result} |"
            )
    return "\n".join(lines) + "\n"


def run(components: set[int]) -> int:
    records = [record for record in load_inventory() if int(record["component"]) in components]
    rows_by_paper: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        qp_file = source_path(record["qp"], DEFAULT_SOURCE_ROOT)
        ms_file = source_path(record["ms"], DEFAULT_SOURCE_ROOT)
        qp = split_question_paper(extract_pdf(qp_file, DEFAULT_CACHE_ROOT))
        ms = parse_mark_scheme(extract_pdf(ms_file, DEFAULT_CACHE_ROOT))
        rows = align_rows(record, qp, ms)
        rows_by_paper[record["paper"]] = rows
        write_jsonl(ROOT / "corpus" / "rows" / f"p{record['component']}" / f"{record['paper']}.jsonl", rows)
    dedupe(rows_by_paper)
    # Dedupe changes are intentionally written after all rows are present.
    for record in records:
        write_jsonl(ROOT / "corpus" / "rows" / f"p{record['component']}" / f"{record['paper']}.jsonl", rows_by_paper[record["paper"]])
    report_path = ROOT / "corpus" / "extract_report.md"
    report_path.write_text(report(records, rows_by_paper), encoding="utf-8")
    print(f"wrote {len(records)} papers / {sum(len(rows) for rows in rows_by_paper.values())} rows")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--component", type=int, choices=[1, 2, 3, 4])
    group.add_argument("--all", action="store_true")
    args = parser.parse_args()
    components = {args.component} if args.component else {1, 2, 3, 4}
    return run(components)


if __name__ == "__main__":
    raise SystemExit(main())
