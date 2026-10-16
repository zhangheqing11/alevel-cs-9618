#!/usr/bin/env python3
"""Build corpus/inventory.csv from sources/pastpapers/ (see schemas/corpus-format.md)."""
from __future__ import annotations

import csv
import hashlib
import os
import pathlib
import re
import sys

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[2]
SOURCES = pathlib.Path(os.environ.get("ALEVEL_CS_SOURCES", "/Users/zhangheqing/Desktop/alevel cs/sources"))
PAST = SOURCES / "pastpapers"
OUT = ROOT / "corpus" / "inventory.csv"
COLS = ["paper", "component", "session", "year", "variant", "corpus", "qp", "ms", "in", "sf",
        "er", "gt", "total_marks", "qp_sha256", "ms_sha256", "duplicate_of", "status"]
QP = re.compile(r"^9618_([msw])(\d{2})_qp_([1-4])([1-3])\.pdf$")


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""


def total_marks(qp: pathlib.Path) -> str:
    with pymupdf.open(qp) as doc:
        text = " ".join(doc[i].get_text() for i in range(min(2, doc.page_count)))
    m = re.search(r"total mark for this paper is (\d+)", text, re.IGNORECASE)
    return m.group(1) if m else ""


def main() -> int:
    rows, seen = [], {}
    for qp in sorted(PAST.glob("9618_*_qp_*.pdf")):
        m = QP.match(qp.name)
        if not m:
            continue
        sess, yy, comp, var = m.groups()
        code, paper = f"{sess}{yy}", f"9618_{sess}{yy}_{comp}{var}"
        ms = PAST / f"9618_{code}_ms_{comp}{var}.pdf"
        ins = PAST / f"9618_{code}_in_{comp}{var}.pdf"
        sf = PAST / f"9618_{code}_sf_{comp}{var}"
        er, gt = PAST / f"9618_{code}_er.pdf", PAST / f"9618_{code}_gt.pdf"
        qsha = sha(qp)
        status = []
        if not ms.exists():
            status.append("missing-ms")
        if comp == "4" and not sf.is_dir():
            status.append("missing-sf")
        if comp == "2" and not ins.exists():
            status.append("missing-in")
        marks = total_marks(qp)
        if not marks:
            status.append("note:total-marks-not-found")
        rows.append({
            "paper": paper, "component": comp, "session": sess, "year": f"20{yy}", "variant": var,
            "corpus": "extension" if yy == "21" else "verified",
            "qp": qp.name, "ms": ms.name if ms.exists() else "", "in": ins.name if ins.exists() else "",
            "sf": sf.name if sf.is_dir() else "", "er": er.name if er.exists() else "",
            "gt": gt.name if gt.exists() else "", "total_marks": marks,
            "qp_sha256": qsha, "ms_sha256": sha(ms), "duplicate_of": seen.get(qsha, ""),
            "status": ";".join(status) or "ok",
        })
        seen.setdefault(qsha, paper)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    bad = [r for r in rows if r["status"] != "ok"]
    print(f"{len(rows)} papers → {OUT.relative_to(ROOT)}; {len(bad)} with status ≠ ok")
    for r in bad:
        print(f"  {r['paper']}: {r['status']}")
    marks = {r["total_marks"] for r in rows}
    print("total_marks values:", marks, "· duplicates:", [r["paper"] for r in rows if r["duplicate_of"]])
    return 0


if __name__ == "__main__":
    sys.exit(main())
