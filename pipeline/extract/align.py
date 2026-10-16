"""Align QP mark boxes with the mark-scheme question cells."""
from __future__ import annotations

import re
from typing import Any

from parse_ms import MSBlock
from split_qp import QPSegment


COMMANDS = re.compile(
    r"^(State|Describe|Explain|Identify|Give|Convert|Complete|Write|Draw|Calculate|Suggest|Compare|"
    r"Discuss|Trace|Test|Amend|Declare|Outline|Name|Define|Determine|Show|Justify|Evaluate|Analyse|"
    r"Implement|Design|Produce|Tick|List|Use|Read|Output|Find|Specify|Provide|Calculate)\b",
    re.I,
)
FIGURE_WORDS = re.compile(
    r"\b(table|diagram|circuit|graph|flowchart|map|array|register|truth table|syntax diagram|"
    r"class diagram|following code|code listing|shown below|shown above|draw|tick|underline|INPUT|pseudocode|following section)\b",
    re.I,
)


def _clean_layout_text(text: str) -> str:
    return text.strip()


def _command_word(stem: str) -> str | None:
    for line in stem.splitlines():
        match = COMMANDS.match(line.strip())
        if match:
            return match.group(1)
    return None


def _figure(stem: str) -> bool:
    return bool(FIGURE_WORDS.search(stem))


def align_rows(
    record: dict[str, str],
    qp_segments: list[QPSegment],
    ms_blocks: list[MSBlock],
) -> list[dict[str, Any]]:
    """Return schema-shaped rows in printed order.

    The QP's printed ``[n]`` is authoritative for marks.  If a source text
    layer ever loses a mark-scheme cell, the row is retained with an explicit
    ``ms-misaligned`` flag rather than inventing an answer.
    """
    rows: list[dict[str, Any]] = []
    ms_by_label = {block.label: block for block in ms_blocks}
    for index, qp in enumerate(qp_segments):
        label = qp.label_hint or str(index + 1)
        ms = ms_by_label.get(label)
        stem = _clean_layout_text(qp.text) if qp is not None else ""
        stem_ctx = _clean_layout_text(qp.context) if qp is not None else ""
        ms_text = ms.text if ms is not None else ""
        flags: list[str] = []
        if qp is None or ms is None or not ms_text:
            flags.append("ms-misaligned")
        if not stem:
            flags.append("split-uncertain")
        if ms is not None and ms.marks != qp.marks:
            flags.append("marks-unclear")
        has_figure = _figure(stem + "\n" + stem_ctx)
        if has_figure:
            flags.append("figure")
        qn_match = re.match(r"(\d+)", label)
        qn = int(qn_match.group(1)) if qn_match else index + 1
        paper = record["paper"]
        rows.append(
            {
                "id": f"{paper}:{label}",
                "paper": paper,
                "component": int(record["component"]),
                "session": record["session"],
                "year": int(record["year"]),
                "variant": int(record["variant"]),
                "q": label,
                "qn": qn,
                "marks": qp.marks if qp is not None else 0,
                "command_word": _command_word(stem),
                "stem": stem,
                "stem_ctx": stem_ctx,
                "qp_page": qp.page if qp is not None else 1,
                "ms_page": ms.page if ms is not None else 1,
                "ms_text": ms_text,
                "has_figure": has_figure,
                "equivalent_of": None,
                "extension": int(record["year"]) == 2021,
                "flags": sorted(set(flags)),
            }
        )
    return rows
