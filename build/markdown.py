"""Markdown assembly, automatic blocks and citation rendering."""

from __future__ import annotations

import html
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Mapping
from urllib.parse import quote

from .stats import COMMAND_LABELS, rows_for_type


ROW_REF = re.compile(r"⟦([^⟧\s]+)⟧")
QUOTE_REF = re.compile(r"「(.*?)」\s*⟦([^⟧\s]+)⟧", re.S)
AUTO_BLOCK = re.compile(r"<!--\s*auto:\s*([a-z-]+)(?:\s+([^\s>]+))?\s*-->")


def paper_short(paper: str) -> str:
    """Turn ``9618_s24_22`` into the compact handbook label ``s24/22``."""

    match = re.match(r"^9618_([msw]\d{2})_([1-4]\d)$", paper)
    return f"{match.group(1)}/{match.group(2)}" if match else paper


def short_question(row_id: str, rows_by_id: Mapping[str, Mapping] | None = None) -> str:
    row = (rows_by_id or {}).get(row_id, {})
    paper, _, question = row_id.partition(":")
    question = str(row.get("q") or question)
    return f"{paper_short(paper)} Q{question}"


def _default_files(row_id: str) -> tuple[str, str]:
    paper = row_id.split(":", 1)[0]
    match = re.match(r"^9618_([msw])(\d{2})_([1-4]\d)$", paper)
    if not match:
        return "QP", "MS"
    session, year, variant = match.groups()
    return (f"9618_{session}{year}_qp_{variant}.pdf",
            f"9618_{session}{year}_ms_{variant}.pdf")


def citation_metadata(rows: Iterable[Mapping], inventory: Mapping[str, Mapping] | None = None,
                      source_root: Path | str | None = None) -> dict[str, dict]:
    """Build tooltip metadata for each corpus row."""

    inv = inventory or {}
    source = Path(source_root or os.environ.get(
        "ALEVEL_CS_SOURCES", "/Users/zhangheqing/Desktop/alevel cs/sources"
    )).expanduser().resolve()
    result: dict[str, dict] = {}
    for row in rows:
        row_id = str(row.get("id", ""))
        if not row_id:
            continue
        qp_default, ms_default = _default_files(row_id)
        paper = str(row.get("paper") or row_id.split(":", 1)[0])
        record = inv.get(paper, {})
        qp = record.get("qp") or qp_default
        ms = record.get("ms") or ms_default
        qp_page = row.get("qp_page", "?")
        ms_page = row.get("ms_page", "?")
        title = f"QP {qp} p.{qp_page}; MS {ms} p.{ms_page}"
        qp_path = source / "pastpapers" / qp
        qp_url = f"file://{quote(str(qp_path), safe='/:@')}#page={qp_page}"
        result[row_id] = {
            "id": row_id,
            "paper": paper,
            "q": str(row.get("q") or row_id.split(":", 1)[-1]),
            "short": short_question(row_id, {row_id: row}),
            "qp": qp,
            "ms": ms,
            "qp_page": qp_page,
            "ms_page": ms_page,
            "title": title,
            "qp_url": qp_url,
        }
    return result


def render_citations(text: str, metadata: Mapping[str, Mapping], *, output: str = "html") -> str:
    """Render row references for Markdown or HTML output.

    Markdown intentionally contains plain text only.  HTML gets a QP PDF link with
    its page fragment and keeps the QP/MS page tooltip for quick source checking.
    """

    combined = re.compile(r"「(.*?)」\s*⟦([^⟧\s]+)⟧|⟦([^⟧\s]+)⟧", re.S)

    def replace(match: re.Match) -> str:
        quote, quoted_id, bare_id = match.groups()
        row_id = quoted_id or bare_id
        info = metadata.get(row_id)
        short = info.get("short", short_question(row_id)) if info else short_question(row_id)
        if output == "md":
            if quote is None:
                return short
            return f'"{quote}" ({short})'
        title = info.get("title", "未找到题卷/评分方案元数据") if info else "未找到题卷/评分方案元数据"
        href = info.get("qp_url", "") if info else ""
        if not href:
            href = "#"
        anchor = f'<a class="citation" href="{html.escape(href, quote=True)}" title="{html.escape(title, quote=True)}">{html.escape(short)}</a>'
        if quote is None:
            return anchor
        # English score sentences are visually distinct while the exact quoted
        # wording remains untouched for the repository's quote checker.
        return f'<span class="score-sentence">“{html.escape(quote)}”</span> {anchor}'

    return combined.sub(replace, text)


def _type_tree(chapter: str, taxonomy: Mapping, stats: Mapping[str, Mapping]) -> str:
    types = [item for item in taxonomy.get("types", []) if item.get("chapter") == chapter]
    if not types:
        return "（本章尚无题型）"
    lines = ["| 题型 | 名称 | 频率 | 小问数 | 分值 |", "|:--|:--|:--:|--:|--:|"]
    for item in types:
        code = item.get("code", "")
        stat = stats.get(code, {})
        lines.append(
            f"| [{code}](#{code}) | {item.get('name_zh', '')} | "
            f"{stat.get('stars', '★☆☆')} | {stat.get('questions', 0)} | {stat.get('marks', 0)} |"
        )
    return "\n".join(lines)


def _chapter_stats(chapter: str | None, taxonomy: Mapping, stats: Mapping[str, Mapping]) -> str:
    if chapter:
        types = [item.get("code") for item in taxonomy.get("types", []) if item.get("chapter") == chapter]
        values = [stats.get(code, {}) for code in types]
        label = next((c.get("name_zh", chapter) for c in taxonomy.get("chapters", []) if c.get("code") == chapter), chapter)
        questions = sum(int(value.get("questions", 0)) for value in values)
        marks = sum(int(value.get("marks", 0)) for value in values)
        papers = len({paper for value in values for paper in value.get("papers", [])})
        sessions = len({session for value in values for session in value.get("sessions", [])})
        return f"**本章考情｜{label}**　核验语料 {questions} 小问 / {marks} 分，涉及 {papers} 卷、{sessions} 个考季。"
    lines = ["| 章节 | 核验小问 | 分值 | 出现卷数 | 考季数 |", "|:--|--:|--:|--:|--:|"]
    for chapter_info in taxonomy.get("chapters", []):
        code = chapter_info.get("code", "")
        type_codes = [item.get("code") for item in taxonomy.get("types", []) if item.get("chapter") == code]
        values = [stats.get(t, {}) for t in type_codes]
        lines.append(
            f"| {code} {chapter_info.get('name_zh', '')} | {sum(int(v.get('questions', 0)) for v in values)} | "
            f"{sum(int(v.get('marks', 0)) for v in values)} | "
            f"{len({p for v in values for p in v.get('papers', [])})} | "
            f"{len({s for v in values for s in v.get('sessions', [])})} |"
        )
    return "\n".join(lines) if len(lines) > 2 else "（暂无语料统计）"


def _one_line_stats(code: str, stats: Mapping[str, Mapping]) -> str:
    value = stats.get(code)
    if not value:
        return f"> **考情**　★☆☆　{code}：暂无核验语料统计。"
    counts = value.get("command_distribution", {})
    distribution = "、".join(f"{label} {counts[key]}" for key, label in COMMAND_LABELS.items()
                             if counts.get(key)) or "暂无设问分布"
    return (
        f"> **考情**　{value.get('stars', '★☆☆')}　{value.get('questions', 0)} 小问 / "
        f"{value.get('marks', 0)} 分；{value.get('paper_count', 0)} 卷、{value.get('session_count', 0)} 考季；"
        f"设问：{distribution}；2021 扩展 {value.get('extension_questions', 0)} 小问。"
    )


def _is_reserved(row: Mapping) -> bool:
    """D1: s26 leaves are reserved for whole-paper mock exams."""
    return str(row.get("paper", "")).startswith("9618_s26_") or (
        str(row.get("session", "")) == "s" and row.get("year") == 2026
    )


def _drill_lines(code: str, rows: Iterable[Mapping]) -> str:
    current = rows_for_type(rows, code, extension=False)
    extension = rows_for_type(rows, code, extension=True)

    def groups(values: list[dict]) -> list[str]:
        grouped: dict[str, list[str]] = defaultdict(list)
        order: list[str] = []
        for row in values:
            paper = str(row.get("paper", ""))
            if paper not in grouped:
                order.append(paper)
            q = str(row.get("q") or row.get("id", "").split(":", 1)[-1])
            if q not in grouped[paper]:
                grouped[paper].append(q)
        return [f"- {paper_short(paper)} " + ", ".join(f"Q{q}" for q in grouped[paper]) for paper in order]

    reserved = [row for row in current if _is_reserved(row)]
    regular = [row for row in current if not _is_reserved(row)]
    lines = groups(regular)
    for line in groups(reserved):
        # Keep the D1 label in front of every paper so reserved rows never look
        # like ordinary targeted drills in the generated handbook.
        lines.append(line.replace("- ", "- 保留整卷（模考）：", 1))
    if extension:
        lines.append("- **2021 扩展**")
        lines.extend(f"  {line[2:]}" for line in groups(extension))
    return "\n".join(lines) if lines else "（暂无对应刷题行）"


def substitute_auto_blocks(text: str, *, chapter: str | None, taxonomy: Mapping,
                           stats: Mapping[str, Mapping], rows: Iterable[Mapping]) -> str:
    """Replace known ``<!-- auto:... -->`` markers in one Markdown document."""

    def replace(match: re.Match) -> str:
        kind, argument = match.groups()
        if kind == "chapter-stats":
            return _chapter_stats(chapter, taxonomy, stats)
        if kind == "type-tree":
            return _type_tree(chapter or "", taxonomy, stats)
        if kind == "stats" and argument:
            return _one_line_stats(argument, stats)
        if kind == "drills" and argument:
            return _drill_lines(argument, rows)
        return match.group(0)

    return AUTO_BLOCK.sub(replace, text)


def process_document(text: str, *, chapter: str | None, taxonomy: Mapping,
                     stats: Mapping[str, Mapping], rows: Iterable[Mapping], metadata: Mapping[str, Mapping],
                     output: str = "md") -> str:
    """Fill auto blocks and render citations in a document."""

    filled = substitute_auto_blocks(text, chapter=chapter, taxonomy=taxonomy, stats=stats, rows=rows)
    return render_citations(filled, metadata, output=output)


def read_json(path: Path, default: object) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default
