#!/usr/bin/env python3
"""Check that the local CIE 9618 source tree is ready to use.

The repository keeps Cambridge PDFs and source-file packages outside Git.  This
small, read-only check makes that setup explicit without changing any existing
command: use ``ALEVEL_CS_SOURCES`` or pass ``--sources`` for a one-off check.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys


DEFAULT_SOURCES = Path("/Users/zhangheqing/Desktop/alevel cs/sources")
REQUIRED_DIRECTORIES = (
    ("pastpapers", "past-paper PDFs and P4 source packages"),
    ("official", "current syllabus and pseudocode guidance"),
    ("official/support", "official learner and candidate-support material"),
    ("official/specimen", "2021 specimen papers"),
)
REQUIRED_FILES = (
    ("official/9618_syllabus_2027-2029.pdf", "2027–2029 syllabus"),
    ("official/9618_syllabus_update_2027-2029.pdf", "2027–2029 syllabus update"),
    ("official/9618_pseudocode_guide_2027-2029.pdf", "2027–2029 pseudocode guide"),
)
PASTPAPER_GLOBS = (
    ("9618_*_qp_*.pdf", "normalized question paper (QP)"),
    ("9618_*_ms_*.pdf", "normalized mark scheme (MS)"),
)


def configured_root(value: str | os.PathLike[str] | None = None, *, env=None) -> tuple[Path, str]:
    """Return the selected source root and how it was selected.

    ``value`` is used by ``--sources``.  Otherwise the environment variable is
    honored, followed by the repository's documented default path.
    """
    if value is not None:
        return Path(value).expanduser(), "--sources"
    environ = os.environ if env is None else env
    raw = environ.get("ALEVEL_CS_SOURCES")
    if raw:
        return Path(raw).expanduser(), "ALEVEL_CS_SOURCES"
    return DEFAULT_SOURCES, "documented default"


def diagnose(root: Path) -> list[str]:
    """Return actionable diagnostics for a source root, without reading PDFs."""
    root = Path(root).expanduser()
    if not root.exists():
        return [f"sources root does not exist: {root}"]
    if not root.is_dir():
        return [f"sources root is not a directory: {root}"]

    issues: list[str] = []
    for relative, purpose in REQUIRED_DIRECTORIES:
        path = root / relative
        if not path.is_dir():
            issues.append(f"missing directory ({purpose}): {path}")
    for relative, purpose in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            issues.append(f"missing file ({purpose}): {path}")

    pastpapers = root / "pastpapers"
    if pastpapers.is_dir():
        for pattern, purpose in PASTPAPER_GLOBS:
            if not any(p.is_file() for p in pastpapers.glob(pattern)):
                issues.append(f"pastpapers has no {purpose} matching {pattern!r}: {pastpapers}")
    return issues


def _print_report(root: Path, source: str, issues: list[str]) -> None:
    print(f"CIE 9618 source check: {root}")
    print(f"source selection: {source}")
    if not issues:
        print("✓ required official directories, files, and QP/MS inputs are present")
        return

    print("✗ source setup is incomplete:")
    for issue in issues:
        print(f"  - {issue}")
    print("Set ALEVEL_CS_SOURCES to the directory containing official/ and pastpapers/.")
    print("Expected core layout:")
    print("  <sources>/official/9618_syllabus_2027-2029.pdf")
    print("  <sources>/official/9618_pseudocode_guide_2027-2029.pdf")
    print("  <sources>/pastpapers/9618_<session><yy>_<qp|ms>_<variant>.pdf")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", metavar="PATH", help="source root to check once")
    args = parser.parse_args(argv)
    root, source = configured_root(args.sources)
    issues = diagnose(root)
    _print_report(root, source, issues)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
