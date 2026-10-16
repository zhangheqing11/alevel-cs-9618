"""Link conservative verbatim duplicates, including shared context and MS."""
from __future__ import annotations

import re


def dedupe(rows_by_paper):
    seen = {}
    ordered = sorted(rows_by_paper, key=lambda p: (int(p[6:8]), p[5], p[-2:]))
    for paper in ordered:
        for row in rows_by_paper[paper]:
            # Figures may have identical text but different wiring or layout.
            # Leave them unlinked until their visual content has been checked.
            if row["has_figure"] or len(row["stem"]) < 24:
                continue
            key = (row["component"], row["marks"], *(re.sub(r"\s+", " ", row[k]).strip()
                   for k in ("stem", "stem_ctx", "ms_text")))
            if key in seen:
                row["equivalent_of"] = seen[key]
            else:
                seen[key] = row["id"]
