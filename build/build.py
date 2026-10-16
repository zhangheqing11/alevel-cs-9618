#!/usr/bin/env python3
"""Build CIE 9618 handbooks from hand-authored Markdown and corpus data."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable, Mapping

if __package__ in (None, ""):
    # When a script lives in ``build/``, Python puts that directory first on
    # sys.path.  It contains our ``html.py`` and ``markdown.py`` modules, which
    # would otherwise shadow the standard-library ``html`` and the third-party
    # ``markdown`` package imported by those modules.
    script_dir = str(Path(__file__).resolve().parent)
    sys.path[:] = [entry for entry in sys.path if entry != script_dir]
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from build.html import render_html
from build.markdown import (citation_metadata, paper_short, process_document, read_json,
                            short_question)
from build.stats import calculate_stats, load_inventory, load_rows, rows_for_type


def _load_taxonomy(path: Path) -> dict:
    value = read_json(path, {})
    return value if isinstance(value, dict) else {}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _display_path(path: Path, root: Path) -> str:
    """Print a repository-relative path when output is under root, else absolute."""
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _citation_entry(row: Mapping, metadata: Mapping[str, Mapping]) -> dict:
    info = metadata.get(str(row.get("id", "")), {})
    return {
        "id": row.get("id", ""),
        "short": info.get("short", short_question(str(row.get("id", "")))),
        "paper": row.get("paper", ""),
        "q": row.get("q", ""),
        "qp_page": row.get("qp_page"),
        "ms_page": row.get("ms_page"),
        "qp": info.get("qp"),
        "ms": info.get("ms"),
    }


def _find_heading_ref(text: str, label: str) -> str | None:
    match = re.search(rf"^####\s*{re.escape(label)}\s*⟦([^⟧\s]+)⟧", text, re.M)
    return match.group(1) if match else None


def _find_next_ref(text: str) -> str | None:
    match = re.search(r"\*\*下一道变式\*\*[^⟦]*⟦([^⟧\s]+)⟧", text)
    return match.group(1) if match else None


def _type_section(text: str, code: str) -> str:
    """Extract one ``### <code>`` card from a chapter file."""
    match = re.search(rf"^###\s+{re.escape(code)}(?:\s|　).*?(?=^###\s+|\Z)", text, re.M | re.S)
    return match.group(0) if match else text


def _practice_index(root: Path, codes: Iterable[str]) -> dict[str, list[str]]:
    wanted = set(codes)
    result = {code: [] for code in wanted}
    practice = Path(root) / "practice"
    if not practice.exists():
        return result
    for path in sorted(practice.rglob("meta.json")):
        data = read_json(path, {})
        if not isinstance(data, dict):
            continue
        path_text = path.parent.relative_to(root).as_posix()
        for code in data.get("types", []) or []:
            if code in result and path_text not in result[code]:
                result[code].append(path_text)
    return result


def _drill_index(rows: Iterable[Mapping], code: str, metadata: Mapping[str, Mapping]) -> list[dict]:
    current = rows_for_type(rows, code, extension=False)
    extension = rows_for_type(rows, code, extension=True)
    entries = []
    for row in [*current, *extension]:
        value = _citation_entry(row, metadata)
        value["extension"] = bool(row.get("extension")) or row.get("year") == 2021
        entries.append(value)
    return entries


def _processed(path: Path, *, root: Path, chapter: str | None, taxonomy: Mapping,
               stats: Mapping[str, Mapping], rows: list[dict], metadata: Mapping[str, Mapping]) -> str:
    return process_document(_read(path), chapter=chapter, taxonomy=taxonomy,
                            stats=stats, rows=rows, metadata=metadata)


def build_component(root: Path, out: Path, component: int) -> bool:
    pdir = root / "papers" / f"p{component}"
    taxonomy_path = pdir / "taxonomy.json"
    if not taxonomy_path.exists():
        print(f"skip P{component}: {taxonomy_path.relative_to(root)} is missing")
        return False
    taxonomy = _load_taxonomy(taxonomy_path)
    rows = load_rows(root, component)
    stats = calculate_stats(rows, taxonomy.get("types", []))
    metadata = citation_metadata(rows, load_inventory(root))
    output_dir = out / f"p{component}"
    output_dir.mkdir(parents=True, exist_ok=True)

    parts: list[str] = []
    front = pdir / "front.md"
    if front.exists():
        parts.append(_processed(front, root=root, chapter=None, taxonomy=taxonomy,
                                stats=stats, rows=rows, metadata=metadata))
    cards_dir = pdir / "cards"
    for chapter in taxonomy.get("chapters", []):
        code = chapter.get("code")
        if not code:
            continue
        path = cards_dir / f"{code}.md"
        if path.exists():
            parts.append(_processed(path, root=root, chapter=code, taxonomy=taxonomy,
                                    stats=stats, rows=rows, metadata=metadata))
    back = pdir / "back.md"
    if back.exists():
        parts.append(_processed(back, root=root, chapter=None, taxonomy=taxonomy,
                                stats=stats, rows=rows, metadata=metadata))

    if parts:
        handbook_md = "\n\n".join(part for part in parts if part.strip())
        stem = f"P{component}题型手册"
        md_path = output_dir / f"{stem}.md"
        _write(md_path, handbook_md)
        _write(output_dir / f"{stem}.html", render_html(handbook_md, stem, "handbook"))
        print(f"built {_display_path(md_path, root)}")
    else:
        print(f"skip P{component}: no front.md, cards or back.md")

    core_parts: list[str] = []
    core_dir = pdir / "core"
    for chapter in taxonomy.get("chapters", []):
        code = chapter.get("code")
        path = core_dir / f"{code}.md"
        if path.exists():
            core_parts.append(_processed(path, root=root, chapter=code, taxonomy=taxonomy,
                                         stats=stats, rows=rows, metadata=metadata))
    if core_parts:
        core_md = "\n\n".join(core_parts)
        stem = f"P{component}{'伪代码与Python对照' if component in (2, 4) else '核心概念'}"
        _write(output_dir / f"{stem}.md", core_md)
        _write(output_dir / f"{stem}.html", render_html(core_md, stem, "core"))
        print(f"built {_display_path(output_dir, root)}/{stem}.md")

    codes = [item.get("code") for item in taxonomy.get("types", []) if item.get("code")]
    practice = _practice_index(root, codes)
    type_index: dict[str, dict] = {}
    # Find representative and next-variation references in the card belonging to
    # each type.  A type can be spread over a chapter file, so search that file.
    card_text = {
        chapter.get("code"): _read(cards_dir / f"{chapter.get('code')}.md")
        for chapter in taxonomy.get("chapters", [])
        if chapter.get("code")
    }
    type_to_card_text = {}
    for item in taxonomy.get("types", []):
        type_to_card_text[item.get("code")] = card_text.get(item.get("chapter"), "")
    for item in taxonomy.get("types", []):
        code = item.get("code")
        if not code:
            continue
        raw_card = _type_section(type_to_card_text.get(code, ""), code)
        representative = _find_heading_ref(raw_card, "代表题精讲")
        variation = _find_next_ref(raw_card)
        type_index[code] = {
            "code": code,
            "chapter": item.get("chapter"),
            "name_zh": item.get("name_zh", ""),
            "name_en": item.get("name_en", ""),
            "summary": item.get("summary", ""),
            "stats": stats.get(code, {}),
            "star": stats.get(code, {}).get("star", 1),
            "stars": stats.get(code, {}).get("stars", "★"),
            "representative": _citation_entry(next((r for r in rows if r.get("id") == representative), {"id": representative or ""}), metadata) if representative else None,
            "next_variation": _citation_entry(next((r for r in rows if r.get("id") == variation), {"id": variation or ""}), metadata) if variation else None,
            "drills": _drill_index(rows, code, metadata),
            "exercise_paths": practice.get(code, []),
        }
    index = {
        "component": component,
        "taxonomy_version": taxonomy.get("version"),
        "chapters": taxonomy.get("chapters", []),
        "types": type_index,
    }
    _write(output_dir / "index.json", json.dumps(index, ensure_ascii=False, indent=2))
    return True


def build_ladder(root: Path, out: Path) -> bool:
    ladder = root / "ladder"
    design = ladder / "design.md"
    levels = sorted((ladder / "levels").glob("L*-*/card.md")) if (ladder / "levels").exists() else []
    if not design.exists() and not levels:
        print(f"skip ladder: {ladder.relative_to(root)} has no design.md or levels")
        return False
    rows = load_rows(root)
    metadata = citation_metadata(rows, load_inventory(root))
    # Ladder documents have no component taxonomy.  Empty context still allows
    # citations and generic blocks in future cards to render.
    empty_taxonomy = {"chapters": [], "types": []}
    documents = []
    if design.exists():
        documents.append(_processed(design, root=root, chapter=None, taxonomy=empty_taxonomy,
                                     stats={}, rows=rows, metadata=metadata))
    level_index = []
    for card in levels:
        documents.append(_processed(card, root=root, chapter=None, taxonomy=empty_taxonomy,
                                    stats={}, rows=rows, metadata=metadata))
        level = card.parent.name
        exercises = []
        for meta in sorted(card.parent.rglob("meta.json")):
            exercises.append(meta.parent.relative_to(root).as_posix())
        level_index.append({"id": level, "card": card.relative_to(root).as_posix(), "exercise_paths": exercises})
    output_dir = out / "ladder"
    output_dir.mkdir(parents=True, exist_ok=True)
    md = "\n\n".join(documents)
    _write(output_dir / "Python阶梯.md", md)
    _write(output_dir / "Python阶梯.html", render_html(md, "Python阶梯", "ladder"))
    exercises = []
    for meta in sorted(ladder.rglob("meta.json")):
        data = read_json(meta, {})
        if isinstance(data, dict):
            exercises.append({"path": meta.parent.relative_to(root).as_posix(), "id": data.get("id"), "title": data.get("title")})
    _write(output_dir / "index.json", json.dumps({"design": design.relative_to(root).as_posix() if design.exists() else None,
                                                   "levels": level_index, "exercises": exercises}, ensure_ascii=False, indent=2))
    print(f"built {_display_path(output_dir, root)}/Python阶梯.md")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("all", "p1", "p2", "p3", "p4", "ladder"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository or fixture root")
    parser.add_argument("--out", type=Path, default=None, help="output directory (default ROOT/output)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    out = (args.out or (root / "output")).resolve()
    if args.command == "ladder":
        build_ladder(root, out)
    elif args.command == "all":
        for component in range(1, 5):
            build_component(root, out, component)
        build_ladder(root, out)
    else:
        build_component(root, out, int(args.command[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
