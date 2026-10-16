#!/usr/bin/env python3
"""Import the teacher's Teach Cambridge export into the normalised sources/ layout.

The export was unzipped (untouched) into sources/teach_cambridge_raw/ and its P4
"Supporting File" zips into sources/teach_cambridge_sf/. This script COPIES
(never moves) files into:

  sources/pastpapers/9618_<s|w|m><yy>_<qp|ms|in|er|gt>_<paper>.pdf
  sources/pastpapers/9618_<s|w|m><yy>_sf_<paper>/          (P4 source files + evidence template)
  sources/official/support/<clean name>                    (ECR, specimen answers, learner guide, SoW, guides)
  sources/official/specimen/9618_y21_sp_<qp|ms|in>_<n>.pdf (+ _sf_4/)

Official copies win: an existing differing file (e.g. an earlier PapaCambridge
download) is replaced and reported.
"""
from __future__ import annotations

import filecmp
import os
import pathlib
import re
import shutil
import sys

SOURCES = pathlib.Path(os.environ.get("ALEVEL_CS_SOURCES", "/Users/zhangheqing/Desktop/alevel cs/sources"))
RAW, SF = SOURCES / "teach_cambridge_raw", SOURCES / "teach_cambridge_sf"
PAST, SUPPORT, SPEC = SOURCES / "pastpapers", SOURCES / "official" / "support", SOURCES / "official" / "specimen"

SESSION = {"March": "m", "June": "s", "November": "w"}
KIND = {"question paper": "qp", "mark scheme": "ms", "insert": "in", "examiner report": "er",
        "grade thresholds": "gt", "supporting file": "sf"}
EXAM = re.compile(r"^9618 Computer Science (March|June|November) (\d{4}) "
                  r"(Question paper|Mark Scheme|Insert|Examiner Report|Grade Thresholds|Supporting File)\s*(\d{2})?\.(pdf|zip)$",
                  re.IGNORECASE)
SPECIMEN = re.compile(r"^9618 Computer Science 2021 Specimen (Question Paper|Mark Scheme|Insert|Paper Support File)\s+(\d)\.(pdf|zip)$")
SUPPORT_KEEP = re.compile(r"Example Candidate Responses|Specimen Paper Answers|Learner Guide|Scheme of Work|Pseudocode Guide|Syllabus")


def copy(src: pathlib.Path, dst: pathlib.Path, log: list[str]) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        return
    if dst.exists():
        if filecmp.cmp(src, dst, shallow=False):
            return
        log.append(f"replaced differing {dst.name} with official copy")
    shutil.copy2(src, dst)


def clean(name: str) -> str:
    return re.sub(r"\s+", "_", re.sub(r"[()]", "", name.replace("9618 ", "9618_"))).replace("_-_", "-")


def main() -> int:
    if not RAW.is_dir():
        print(f"missing {RAW}")
        return 1
    log: list[str] = []
    counts: dict[str, int] = {}
    unknown = []
    for src in sorted(RAW.iterdir()):
        name = src.name
        m = EXAM.match(name)
        if m:
            sess, year, kind, paper, ext = m.groups()
            code = f"{SESSION[sess]}{year[2:]}"
            k = KIND[kind.lower()]
            if k == "sf":
                folder = SF / src.stem
                copy(folder, PAST / f"9618_{code}_sf_{paper}", log)
            else:
                stem = f"9618_{code}_{k}_{paper}" if paper else f"9618_{code}_{k}"
                copy(src, PAST / f"{stem}.{ext}", log)
            counts[k] = counts.get(k, 0) + 1
            continue
        m = SPECIMEN.match(name)
        if m:
            kind, n, ext = m.groups()
            k = {"Question Paper": "qp", "Mark Scheme": "ms", "Insert": "in", "Paper Support File": "sf"}[kind]
            if ext == "zip":
                copy(SF / src.stem, SPEC / f"9618_y21_sp_{'qp' if k == 'qp' else 'sf'}_{n}", log)
            else:
                copy(src, SPEC / f"9618_y21_sp_{k}_{n}.pdf", log)
            counts["specimen"] = counts.get("specimen", 0) + 1
            continue
        if SUPPORT_KEEP.search(name):
            copy(src, SUPPORT / clean(name), log)
            counts["support"] = counts.get("support", 0) + 1
            continue
        unknown.append(name)
    print("imported:", counts)
    for line in log:
        print("  ·", line)
    print(f"skipped {len(unknown)} (copyright booklets, unrelated):")
    for n in unknown:
        print("  -", n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
