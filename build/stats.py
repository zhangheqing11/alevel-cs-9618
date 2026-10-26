"""Load corpus rows and calculate question-type statistics.

The builder deliberately keeps statistics independent of Markdown rendering.  This
makes the values useful to tests and to the JSON index as well as to the handbook.
"""

from __future__ import annotations

import collections
import csv
import json
import re
from pathlib import Path
from typing import Iterable, Mapping


# Stable machine keys; presentation labels are kept separate for Markdown/HTML.
COMMAND_LABELS = {
    "state": "陈述/识别/列举",
    "describe": "描述",
    "explain": "解释/论证",
    "complete": "补全/绘制",
    "write": "编写（代码/表达式/SQL）",
    "calculate": "计算/转换",
    "compare": "比较/评价",
    "other": "其他",
}
COMMAND_GROUPS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("state", ("state", "identify", "give", "name", "define", "list", "label")),
    ("describe", ("describe", "outline")),
    ("explain", ("explain", "justify", "why", "suggest")),
    ("complete", ("complete", "draw", "fill", "trace", "dry run", "tick", "circle", "match", "copy")),
    ("write", ("write", "code", "program", "implement", "construct")),
    ("calculate", ("calculate", "convert", "show", "work out", "determine", "find")),
    ("compare", ("compare", "evaluate", "discuss", "distinguish", "difference", "contrast")),
)
# Larger values are later in the exam year; reverse sorting therefore puts a
# same-year winter (w) paper before a summer (s) paper.
SESSION_ORDER = {"m": 1, "s": 2, "w": 3}


def load_rows(root: Path, component: int | None = None) -> list[dict]:
    """Read JSONL rows in deterministic order, ignoring blank lines.

    A missing rows directory is a valid state while the corpus is being built.  A
    malformed line is skipped so ``make build`` can still produce the other books;
    the repository validator remains responsible for reporting malformed corpus.
    """

    rows_root = Path(root) / "corpus" / "rows"
    pattern = f"p{component}" if component else "p[1-4]"
    rows: list[dict] = []
    for path in sorted(rows_root.glob(f"{pattern}/*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                rows.append(value)
    return rows


def load_inventory(root: Path) -> dict[str, dict]:
    """Return inventory rows keyed by paper id, when the inventory exists."""

    path = Path(root) / "corpus" / "inventory.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return {row.get("paper", ""): row for row in csv.DictReader(stream) if row.get("paper")}


def command_group(command_word: object) -> str:
    """Group the leading command phrase; missing/unknown commands stay other."""

    text = re.sub(r"\s+", " ", str(command_word or "").strip().lower())
    for group, prefixes in COMMAND_GROUPS:
        if any(re.match(rf"^{re.escape(prefix)}\b", text) for prefix in prefixes):
            return group
    return "other"


def _row_types(row: Mapping) -> tuple[str | None, list[str]]:
    typed = row.get("types")
    if isinstance(typed, Mapping):
        primary = typed.get("primary")
        cross = typed.get("cross", [])
    else:
        primary = row.get("primary") or row.get("type")
        cross = row.get("cross", [])
    if isinstance(cross, str):
        cross = [cross]
    return (primary if isinstance(primary, str) else None,
            [item for item in cross if isinstance(item, str)])


def _blank(code: str, taxonomy: Mapping | None = None) -> dict:
    item = {
        "code": code,
        "name_zh": (taxonomy or {}).get("name_zh", ""),
        "name_en": (taxonomy or {}).get("name_en", ""),
        "summary": (taxonomy or {}).get("summary", ""),
        "questions": 0,
        "marks": 0,
        "cross_questions": 0,
        "cross_chapters": 0,
        "cross_papers": [],
        "cross_sessions": [],
        "papers": [],
        "sessions": [],
        "command_words": {},
        "extension_questions": 0,
        "extension_marks": 0,
        "score": 0,
        "star": 1,
        "stars": "★☆☆",
        "representative_questions": [],
    }
    return item


def _session_label(row: Mapping) -> str:
    session = str(row.get("session", ""))
    year = row.get("year")
    try:
        return f"{session}{int(year) % 100:02d}"
    except (TypeError, ValueError):
        return session


def calculate_stats(rows: Iterable[Mapping], taxonomy_types: Iterable[Mapping] = ()) -> dict[str, dict]:
    """Calculate primary, cross and extension counts for every taxonomy type.

    Verified statistics exclude rows marked ``extension`` and rows with
    ``equivalent_of``.  Extension rows are retained only in the explicit 2021
    extension counters.  Cross occurrences never increase the primary question or
    mark totals.
    """

    tax = {item.get("code"): item for item in taxonomy_types if item.get("code")}
    stats = {code: _blank(code, value) for code, value in tax.items()}
    all_rows = list(rows)

    # Include tagged types that are not yet present in a taxonomy fixture.  This is
    # useful for an in-progress corpus, while a normal make check will catch the
    # taxonomy mismatch separately.
    for row in all_rows:
        primary, cross = _row_types(row)
        for code in [primary, *cross]:
            if code and code not in stats:
                stats[code] = _blank(code)

    verified = []
    for row in all_rows:
        is_extension = bool(row.get("extension")) or row.get("year") == 2021
        equivalent = bool(row.get("equivalent_of"))
        primary, cross = _row_types(row)
        if is_extension:
            if primary in stats:
                stats[primary]["extension_questions"] += 1
                stats[primary]["extension_marks"] += int(row.get("marks") or 0)
            continue
        if equivalent:
            continue
        verified.append(row)
        marks = int(row.get("marks") or 0)
        if primary in stats:
            item = stats[primary]
            item["questions"] += 1
            item["marks"] += marks
            item["papers"].append(str(row.get("paper", "")))
            item["sessions"].append(_session_label(row))
            group = command_group(row.get("command_word"))
            item["command_words"][group] = item["command_words"].get(group, 0) + 1
            item["representative_questions"].append(str(row.get("id", "")))
        for code in cross:
            if code in stats:
                stats[code]["cross_questions"] += 1
                # The chapter code is the stable part of a type code.  A set would
                # lose occurrence counts, so track private values until finalizing.
                stats[code].setdefault("_cross_chapter_values", set()).add(code.split("-")[1])
                stats[code]["cross_papers"].append(str(row.get("paper", "")))
                stats[code]["cross_sessions"].append(_session_label(row))

    for item in stats.values():
        item["papers"] = sorted({p for p in item["papers"] if p})
        item["sessions"] = sorted({s for s in item["sessions"] if s})
        item["cross_papers"] = sorted({p for p in item["cross_papers"] if p})
        item["cross_sessions"] = sorted({s for s in item["cross_sessions"] if s})
        item["paper_count"] = len(item["papers"])
        item["session_count"] = len(item["sessions"])
        item["cross_paper_count"] = len(item["cross_papers"])
        item["cross_session_count"] = len(item["cross_sessions"])
        item["question_count"] = item["questions"]
        item["mark_count"] = item["marks"]
        item["cross_count"] = item["cross_questions"]
        item["extension_count"] = item["extension_questions"]
        item["command_distribution"] = dict(sorted(item["command_words"].items()))
        item["cross_chapters"] = len(item.pop("_cross_chapter_values", set()))
        item["cross_chapter_occurrences"] = item["cross_questions"]
        item["score"] = item["marks"] + 3 * item["session_count"]

    apply_stars(stats)
    return stats


def apply_stars(stats: Mapping[str, dict]) -> None:
    """Apply the physics-compatible 1/4 and 2/3 score cutoffs in place."""

    values = sorted((int(item.get("score", 0)) for item in stats.values()), reverse=True)
    if not values:
        return
    first_cut = values[min(len(values) - 1, len(values) // 4)]
    second_cut = values[min(len(values) - 1, (len(values) * 2) // 3)]
    for item in stats.values():
        score = int(item.get("score", 0))
        star = 3 if score >= first_cut else 2 if score >= second_cut else 1
        item["star"] = star
        item["stars"] = "★" * star + "☆" * (3 - star)


def rows_for_type(rows: Iterable[Mapping], code: str, *, extension: bool | None = None) -> list[dict]:
    """Return rows where *code* is primary or cross, sorted newest first."""

    found: list[dict] = []
    for row in rows:
        is_extension = bool(row.get("extension")) or row.get("year") == 2021
        if extension is not None and is_extension != extension:
            continue
        if extension is False and row.get("equivalent_of"):
            continue
        primary, cross = _row_types(row)
        if code == primary or code in cross:
            found.append(dict(row))

    # Newer papers come first, while leaves within one paper retain exam order.
    # Sorting the complete tuple in reverse would incorrectly put Q2 after Q1's
    # subparts, so sort papers first and each paper's question labels separately.
    paper_order = sorted({str(row.get("paper", "")) for row in found}, key=lambda paper: (
        int(next((r.get("year", 0) for r in found if r.get("paper") == paper), 0) or 0),
        SESSION_ORDER.get(str(next((r.get("session", "") for r in found if r.get("paper") == paper), "")), -1),
        paper,
    ), reverse=True)

    def question_key(row: Mapping) -> list[object]:
        value = str(row.get("q", row.get("id", "")))
        result: list[object] = []
        for token in re.findall(r"\d+|[A-Za-z]+", value):
            result.append(int(token) if token.isdigit() else token.lower())
        return result

    return [row for paper in paper_order for row in sorted(
        (row for row in found if str(row.get("paper", "")) == paper), key=question_key
    )]


def stats_for_component(root: Path, component: int, taxonomy: Mapping) -> tuple[list[dict], dict[str, dict]]:
    """Convenience wrapper used by the CLI."""

    rows = load_rows(root, component)
    types = taxonomy.get("types", []) if isinstance(taxonomy, Mapping) else []
    return rows, calculate_stats(rows, types)
