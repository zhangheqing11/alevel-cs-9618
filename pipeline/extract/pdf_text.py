"""PDF text helpers for the T12 corpus extractor.

The source PDFs stay outside the repository.  This module caches both a
layout text export (useful for readable stems) and PyMuPDF word coordinates
(used to identify the right-margin mark boxes without confusing table labels
such as ``[1] [2] [3]`` with question marks).
"""
from __future__ import annotations

import json
import os
import pathlib
import shutil
import subprocess
from typing import Any


DEFAULT_SOURCE_ROOT = pathlib.Path(
    os.environ.get("ALEVEL_CS_SOURCES", "/Users/zhangheqing/Desktop/alevel cs/sources")
)
DEFAULT_CACHE_ROOT = pathlib.Path(
    os.environ.get("ALEVEL_CS_EXTRACT_CACHE", "/tmp/alevel-cs-extract")
)


def source_path(filename: str, source_root: pathlib.Path = DEFAULT_SOURCE_ROOT) -> pathlib.Path:
    return source_root / "pastpapers" / filename


def cache_path(pdf: pathlib.Path, cache_root: pathlib.Path = DEFAULT_CACHE_ROOT) -> pathlib.Path:
    return cache_root / (pdf.name + ".json")


def _layout_text(pdf: pathlib.Path) -> str:
    if shutil.which("pdftotext"):
        proc = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"],
            check=True,
            capture_output=True,
        )
        return proc.stdout.decode("utf-8", "replace")
    return ""


def _word_pages(pdf: pathlib.Path) -> list[list[dict[str, Any]]]:
    import pymupdf

    doc = pymupdf.open(pdf)
    pages: list[list[dict[str, Any]]] = []
    for page in doc:
        words = []
        for x0, y0, x1, y1, text, block, line, word in page.get_text("words", sort=True):
            rect = pymupdf.Rect(x0, y0, x1, y1) * page.rotation_matrix
            x0, y0, x1, y1 = rect
            words.append(
                {
                    "x0": round(float(x0), 3),
                    "y0": round(float(y0), 3),
                    "x1": round(float(x1), 3),
                    "y1": round(float(y1), 3),
                    "text": text,
                    "block": int(block),
                    "line": int(line),
                    "word": int(word),
                }
            )
        pages.append(words)
    return pages


def extract_pdf(pdf: pathlib.Path, cache_root: pathlib.Path = DEFAULT_CACHE_ROOT) -> dict[str, Any]:
    """Extract and cache a PDF without changing the source file."""
    cache_root.mkdir(parents=True, exist_ok=True)
    out = cache_path(pdf, cache_root)
    if out.exists() and out.stat().st_mtime >= pdf.stat().st_mtime:
        cached = json.loads(out.read_text(encoding="utf-8"))
        if cached.get("version") == 2:
            return cached
    data = {"version": 2, "pdf": str(pdf), "layout": _layout_text(pdf), "word_pages": _word_pages(pdf)}
    out.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data
