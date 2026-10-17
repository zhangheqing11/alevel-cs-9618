"""Rebuild T12 JSONL rows and the extraction report.

Examples:
    python pipeline/extract/run_all.py --component 1
    python pipeline/extract/run_all.py --all
"""
from __future__ import annotations

import argparse
import csv
import json
import hashlib
import pathlib
import random
from collections import Counter
from typing import Any

from align import align_rows
from dedupe import dedupe
from normalise import normalise_row
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


def row_hash(row):
    base = {k: v for k, v in row.items() if k not in
            {'types', 'tag_confidence', 'tag_note', 'markpoints', 'ms_max', 'er'}}
    return hashlib.sha256(json.dumps(base, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def report(selected, rows_by_paper):
    flags = ["split-uncertain", "ms-misaligned", "marks-unclear", "figure", "ocr-garbled", "needs-review"]
    audits = {}
    overrides = json.loads((ROOT / "pipeline/extract/overrides.json").read_text(encoding="utf-8"))
    for path in sorted((ROOT / "pipeline/extract").glob("audit_p*.json")):
        for entry in json.loads(path.read_text(encoding="utf-8")):
            audits[entry["id"]] = entry
    lines = [
        "# T12 抽取报告", "",
        "生成命令：`python pipeline/extract/run_all.py --component N`（N 为本次批次卷号，或 `--all`）；报告累积保留已有批次。",
        "源 PDF：`$ALEVEL_CS_SOURCES/pastpapers/`，只读；缓存：`/tmp/alevel-cs-extract/`。",
        "", "## 方法与核验边界", "",
        "- QP 从 PDF 坐标识别实际最细题号和右侧 `[n]` 分值；不把数组下标当分值，不为凑总分拆题。",
        "- MS 按同季同年同 variant、同题号对齐，只抽 Answer 列；重复题号的语言示例与无表头续页连续保留。Marks 列单独比对，Guidance 列未混入 `ms_text`。",
        "- 表格、代码尽量以坐标重建列位。文字层无法表达连线、阴影、下划线、逻辑取反横线及部分图形箭头；相关行标 `figure`，图形的完整语义以 QP/MS 原页为准。",
        "- `stem_ctx` 保留可直接继承的父级情景；题目引用的其他小问仍按题号回看，未把相邻小问当成本题题干。",
        "- `equivalent_of` 采用保守的逐字比较：相同卷别、分值、题干、父级情景及 MS（只忽略空白），按年/季排序；图形行未仅凭相同文字判重。",
        "- 2021 标 `extension: true`；s26 全量入库。模考保留规则由下游执行。T12 不写 types/tag_confidence/markpoints/er。",
        "", "## 卷级统计", "",
        "| 卷 | 行数 | 分值和 | " + " | ".join(flags) + " |",
        "|---|---:|---:|" + "---:|" * len(flags),
    ]
    all_rows = []
    for record in selected:
        rows = rows_by_paper[record["paper"]]
        all_rows.extend(rows)
        counts = Counter(f for row in rows for f in row["flags"])
        lines.append(f"| {record['paper']} | {len(rows)} | {sum(row['marks'] for row in rows)} | " +
                     " | ".join(str(counts[f]) for f in flags) + " |")
    counts = Counter(f for row in all_rows for f in row["flags"])
    n_uncertain = sum(bool({"ms-misaligned", "split-uncertain"}.intersection(row["flags"])) for row in all_rows)
    lines += ["", f"总计 {len(selected)} 卷、{len(all_rows)} 行、{sum(r['marks'] for r in all_rows)} 分；"
              f"extension {sum(r['extension'] for r in all_rows)} 行；保守重复链接 {sum(r['equivalent_of'] is not None for r in all_rows)} 行。",
              f"`ms-misaligned` / `split-uncertain` 涉及 {n_uncertain} 行（{n_uncertain / max(1, len(all_rows)):.2%}）；"
              + "、".join(f"{f}={counts[f]}" for f in flags) + "。",
              "", "## 未解决问题与源文件差异", ""]
    issues = [r for r in all_rows if set(r["flags"]) - {"figure"}]
    if issues:
        for row in issues:
            note = ": " + overrides[row["id"]]["reason"] if row["id"] in overrides else ""
            if row["id"] == "9618_s25_12:7(b)(ii)":
                note = "：QP p.16 印 [1]；MS p.12 的 Answer 为 1 mark for: / 0000 0011，但右侧 Marks 单元格为空（已查看渲染原页）。保留 QP 的 marks=1，标 marks-unclear，不补造 MS Marks 列。"
            lines.append(f"- `{row['id']}`：{', '.join(f for f in row['flags'] if f != 'figure')}{note}")
    else:
        lines.append("- 无未解决的拆分、对齐或分值差异。")
    lines += ["- MS 文本层题号缺括号：s22_13 的 `5(b(iii)`、w23_42 的 `3(b(iii)`，通用规则只修正题号括号；Answer 内容照原文保留。",
              "- 图形行的 figure 标记不是解析成功的替代证明；使用连线、阴影、箭头、上划线或下划线给分时必须回原页。",
              "", "## 每卷随机 5 行人工抽查", "",
              "固定随机种子为卷号（Random(paper).sample(..., 5)）。记录中的所见来自源 PDF 文字层与相应原页渲染。",
              "核验范围：题号、题干起句/关键数据、分值框、QP/MS 起始页与同题 MS 起句；图表/代码布局另看原页。不是对全部语料逐字人工校勘。",
              "人工记录存于 `pipeline/extract/audit_p*.json`，附行内容 SHA-256；行内容变化后记录自动作废，须复核。未核验不能写一致。", "",
              "| 卷/小问 | QP / MS 页 | 分值 | 所见 | 核验结果 |", "|---|---|---:|---|---|"]
    for record in selected:
        for row in _sample(rows_by_paper[record["paper"]], record["paper"]):
            audit = audits.get(row["id"])
            if not audit or audit.get("row_sha256") != row_hash(row):
                observation, result = "尚无有效人工记录", "待核验"
            else:
                observation = "QP: " + audit["qp_excerpt"] + " / MS: " + audit["ms_excerpt"]
                observation = observation.replace("|", "\\|").replace("\n", " ")
                result = audit["result"]
            lines.append(f"| `{row['id']}` | {row['qp_page']} / {row['ms_page']} | {row['marks']} | {observation} | {result} |")
    return "\n".join(lines) + "\n"


def run(components: set[int]) -> int:
    records = [record for record in load_inventory() if int(record["component"]) in components]
    rows_by_paper = {}
    overrides = json.loads((ROOT / "pipeline/extract/overrides.json").read_text(encoding="utf-8"))
    for record in records:
        qp_file = source_path(record["qp"], DEFAULT_SOURCE_ROOT)
        ms_file = source_path(record["ms"], DEFAULT_SOURCE_ROOT)
        for kind, path in (("qp", qp_file), ("ms", ms_file)):
            expected = record[kind + "_sha256"]
            if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError(f"{record['paper']} {kind}: PDF checksum differs from inventory")
        qp = split_question_paper(extract_pdf(qp_file, DEFAULT_CACHE_ROOT))
        ms = parse_mark_scheme(extract_pdf(ms_file, DEFAULT_CACHE_ROOT))
        q_labels = [q.label_hint for q in qp]
        ms_labels = [block.label for block in ms]
        if len(q_labels) != len(set(q_labels)) or q_labels != ms_labels:
            raise ValueError(f"{record['paper']}: QP/MS labels/order mismatch; inspect source PDFs")
        if sum(q.marks for q in qp) != int(record["total_marks"]):
            raise ValueError(f"{record['paper']}: printed QP marks differ from inventory")
        rows = align_rows(record, qp, ms)
        for row in rows:
            override = overrides.get(row["id"])
            if override:
                if not override.get("reason"):
                    raise ValueError(f"{row['id']}: override has no evidence/reason")
                row.update(override["fields"])
        rows_by_paper[record["paper"]] = rows
    dedupe(rows_by_paper)
    # Normalize only after structural decisions, including duplicate links.
    for rows in rows_by_paper.values():
        for row in rows:
            normalise_row(row)
    # Dedupe changes are intentionally written after all rows are present.
    for record in records:
        write_jsonl(ROOT / "corpus" / "rows" / f"p{record['component']}" / f"{record['paper']}.jsonl", rows_by_paper[record["paper"]])
    # Retain earlier batches in the cumulative report without rewriting them.
    existing_records = []
    for record in load_inventory():
        path = ROOT / "corpus/rows" / f"p{record['component']}" / f"{record['paper']}.jsonl"
        if path.exists():
            existing_records.append(record)
            if record["paper"] not in rows_by_paper:
                rows_by_paper[record["paper"]] = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    report_path = ROOT / "corpus/extract_report.md"
    report_path.write_text(report(existing_records, rows_by_paper), encoding="utf-8")
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
