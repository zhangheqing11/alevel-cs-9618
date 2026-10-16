"""Split QPs by printed labels and coordinate-identified mark boxes."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

ROMAN = r"viii|vii|iii|vi|iv|ii|ix|x|v|i"


@dataclass
class QPSegment:
    marks: int
    page: int
    text: str
    label_hint: str | None
    context: str = ""
    end_page: int = 1
    start_y: float = 0
    end_y: float = 0


def visual_lines(words: list[dict[str, Any]], x_min: float = 44, x_max: float = 552):
    """Rejoin independent PDF text blocks by baseline; retain table columns."""
    groups: list[list[dict[str, Any]]] = []
    for word in sorted(words, key=lambda w: (w["y0"], w["x0"])):
        if word["x0"] < x_min or word["x0"] > x_max:
            continue
        if groups and abs(word["y0"] - min(w["y0"] for w in groups[-1])) < 3:
            groups[-1].append(word)
        else:
            groups.append([word])
    return [sorted(group, key=lambda w: w["x0"]) for group in groups]


def layout_line(words: list[dict[str, Any]], origin: float = 49.6) -> str:
    result = ""
    last_right = origin
    for word in words:
        gap = max(1, round((word["x0"] - last_right) / 5.5))
        if not result:
            result = " " * max(0, round((word["x0"] - origin) / 5.5))
        else:
            result += " " * gap
        result += word["text"]
        last_right = word["x1"]
    return result.rstrip()


def _mark(words):
    for w in words:
        m = re.fullmatch(r"\[(\d+)\]", w["text"])
        if m and w["x0"] > 520:
            return int(m[1]), w
        m = re.fullmatch(r"\.+\[(\d+)\]", w["text"])
        if m:
            return int(m[1]), w
    return None


def _label(words, num: str | None, letter: str | None):
    first = words[0]
    text = " ".join(w["text"] for w in words)
    x = first["x0"]
    if 44 <= x <= 61:
        m = re.match(r"^(\d{1,2})(?:\s+|$)", text)
        if m and int(m[1]) <= 20 and (num is None or int(m[1]) in {int(num), int(num) + 1}):
            number = m[1]
            used = 1
            suffix = ""
            if len(words) > used and re.fullmatch(r"\([a-z]\)", words[used]["text"]):
                suffix += words[used]["text"]
                used += 1
                if len(words) > used and re.fullmatch(rf"\((?:{ROMAN})\)", words[used]["text"]):
                    suffix += words[used]["text"]
                    used += 1
            return number + suffix, words[used:]
    if 65 <= x <= 82 and re.fullmatch(r"\([a-z]\)", first["text"]) and num:
        label = num + first["text"]
        used = 1
        if len(words) > used and re.fullmatch(rf"\((?:{ROMAN})\)", words[used]["text"]):
            label += words[used]["text"]
            used += 1
        return label, words[used:]
    if 85 <= x <= 108 and re.fullmatch(rf"\((?:{ROMAN})\)", first["text"]) and num:
        return num + (letter or "") + first["text"], words[1:]
    return None


def split_question_paper(data: dict[str, Any]) -> list[QPSegment]:
    nodes: dict[str, dict] = {}
    segments = []
    current = None
    number = letter = None
    for pn, words in enumerate(data["word_pages"], 1):
        if pn == 1:
            continue
        for group in visual_lines(words):
            y = min(w["y0"] for w in group)
            if y < 55 or y > 795:
                continue
            text = " ".join(w["text"] for w in group)
            if any(t in text for t in ("©", "UCLES", "9618/", "[Turn", "BLANK PAGE")):
                continue
            # Barcode glyphs are not question content. Margin text is outside
            # the body x range and removed before line reconstruction.
            if any(ord(c) < 32 for c in text) or any(t in text for t in ("Ĭ", "ĥ")):
                continue
            label_info = _label(group, number, letter)
            if label_info:
                label, content = label_info
                m = re.match(r"(\d+)(\([a-z]\))?", label)
                number, letter = m[1], m[2]
                current = label
                nodes[label] = {"lines": [], "page": pn, "y": y, "marked": False}
                if content and not _mark(group):
                    nodes[label]["lines"].append(layout_line(content))
                if _mark(group):
                    group = content
                if not _mark(group):
                    continue
            mark_info = _mark(group)
            if mark_info and current:
                value, mark_word = mark_info
                node = nodes[current]
                content = [w for w in group if w is not mark_word]
                if content:
                    node["lines"].append(layout_line(content))
                ancestors = []
                parent = current
                while "(" in parent:
                    parent = parent[:parent.rfind("(")]
                    if parent in nodes:
                        ancestors.insert(0, "\n".join(nodes[parent]["lines"]))
                segments.append(QPSegment(
                    value, node["page"], "\n".join(node["lines"]).strip(), current,
                    "\n\n".join(x.strip() for x in ancestors if x.strip()), pn, node["y"], y,
                ))
                node["marked"] = True
                continue
            if current and not nodes[current]["marked"]:
                nodes[current]["lines"].append(layout_line(group))
    return segments
