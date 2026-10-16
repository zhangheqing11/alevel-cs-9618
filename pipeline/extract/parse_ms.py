"""Read only the Answer cells of each exact paired mark scheme."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any
from split_qp import visual_lines, layout_line

ROMAN = r"viii|vii|iii|vi|iv|ii|ix|x|v|i"
LABEL = re.compile(rf"^\d+(?:\([a-z]\))?(?:\((?:{ROMAN})\))?$|^\d+\([a-z]\((?:{ROMAN})\)$")


@dataclass
class MSBlock:
    label: str
    page: int
    lines: list[str] = field(default_factory=list)
    marks: int | None = None

    @property
    def text(self):
        return "\n".join(self.lines).strip()


def normalize_label(raw):
    m = re.fullmatch(rf"(\d+)\(([a-z])\(({ROMAN})\)", raw)
    return f"{m[1]}({m[2]})({m[3]})" if m else raw


def parse_mark_scheme(data: dict[str, Any]) -> list[MSBlock]:
    blocks = []
    by_label = {}
    current = None
    answer_left = answer_right = marks_left = marks_right = 0
    active = False
    for pn, words in enumerate(data["word_pages"], 1):
        bottom = 560 if max(w["x1"] for w in words) > 600 else 808
        page_active = active
        for group in visual_lines(words, 15, 810):
            text = " ".join(w["text"] for w in group)
            y = min(w["y0"] for w in group)
            if y < 50 or y > bottom or "©" in text:
                continue
            tokens = {w["text"]: w for w in group}
            if all(x in tokens for x in ("Question", "Answer", "Marks")):
                active = page_active = True
                question_left = tokens["Question"]["x0"]
                answer_left = tokens["Question"]["x1"] + 4
                marks_left = tokens["Marks"]["x0"] - 8
                marks_right = tokens["Marks"]["x1"] + 8
                answer_right = marks_left
                continue
            if not active or not page_active:
                continue
            if "9618/" in text or "PUBLISHED" in text:
                continue
            label_words = [group[0]] if group[0]["x0"] < answer_left and LABEL.fullmatch(group[0]["text"]) and group[0]["text"] != "0" else []
            if label_words:
                label = normalize_label(label_words[0]["text"])
                if label not in by_label:
                    current = MSBlock(label, pn)
                    by_label[label] = current
                    blocks.append(current)
                else:
                    current = by_label[label]
            if current is None:
                continue
            mark_words = [w for w in group if marks_left <= w["x0"] <= marks_right and re.fullmatch(r"\d{1,2}", w["text"])]
            if mark_words and current.marks is None:
                current.marks = int(mark_words[0]["text"])
            answer_words = [w for w in group if question_left <= w["x0"] < answer_right and w not in label_words]
            if answer_words:
                current.lines.append(layout_line(answer_words, answer_left))
    return blocks
