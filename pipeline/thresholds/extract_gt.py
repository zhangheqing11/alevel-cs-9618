#!/usr/bin/env python3
"""Extract the ten 9618 threshold PDFs using Poppler; never edit source PDFs."""
import argparse
import csv
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCES = Path("/Users/zhangheqing/Desktop/alevel cs/sources")
COMPONENTS = tuple(f"{paper}{variant}" for paper in range(1, 5) for variant in range(1, 4))
COMPONENT_FIELDS = ["session", "year", "component", "max_raw", "A", "B", "C", "D", "E"]
OPTION_FIELDS = ["session", "year", "option", "components", "max_weighted", "A*", "A", "B", "C", "D", "E"]


def parse_text(text, session, year):
    """Preserve printed cell strings; an absent component has empty numeric cells."""
    components, options = {}, {}
    for line in text.splitlines():
        match = re.match(r"^\s*Component\s+(\d{2})\s+(.+)$", line)
        if match:
            code, tail = match.groups()
            cells = tail.split()
            if len(cells) != 6 or not all(re.fullmatch(r"\d+|[–—-]", cell) for cell in cells):
                raise ValueError(f"Malformed component row: {line}")
            if code in components:
                raise ValueError(f"Duplicate component: {code}")
            components[code] = dict(zip(COMPONENT_FIELDS, [session, str(year), code, *cells]))
            continue
        if not re.match(r"^\s*[A-Z0-9]{2,3}\s{2,}\d", line):
            continue
        cells = re.split(r"\s{2,}", line.strip())
        if len(cells) == 8:
            # Only 2021 omits the per-option maximum column. Its prose supplies
            # 300 (A Level) / 150 (AS). A2-only maxima are not stated.
            if year != 2021 or not re.search(r"300 for A Level and 150 for\s+AS Level", text):
                raise ValueError(f"Missing maximum without supporting prose: {line}")
            maximum = "" if cells[0].endswith("J") else ("150" if cells[0].startswith("S") else "300")
            cells.insert(1, maximum)
        if len(cells) != 9:
            raise ValueError(f"Malformed option row: {line}")
        code, maximum, combination, *grades = cells
        if ((maximum != "" and not maximum.isdigit()) or not re.fullmatch(r"\d{2}(?:,\s*\d{2})*", combination)
                or not all(re.fullmatch(r"\d+|[–—-]", cell) for cell in grades)):
            raise ValueError(f"Malformed option cells: {line}")
        if code in options:
            raise ValueError(f"Duplicate option: {code}")
        combination = ";".join(part.strip() for part in combination.split(","))
        options[code] = dict(zip(OPTION_FIELDS, [session, str(year), code, combination, maximum, *grades]))
    primary = [components.get(code, dict(zip(COMPONENT_FIELDS, [session, str(year), code, *([""] * 6)])))
               for code in COMPONENTS]
    extras = [row for code, row in components.items() if code not in COMPONENTS]
    return primary, list(options.values()), extras


def pdf_text(path):
    return subprocess.run(["pdftotext", "-layout", str(path), "-"], check=True,
                          capture_output=True, text=True, encoding="utf-8").stdout


def extract(sources):
    components, options, extras = [], [], []
    for year in range(2021, 2026):
        for session in ("s", "w"):
            path = sources / "pastpapers" / f"9618_{session}{year % 100:02}_gt.pdf"
            text = pdf_text(path)
            month = "June" if session == "s" else "November"
            if not re.search(rf"Grade thresholds\s*[–-]\s*{month} {year}", text):
                raise ValueError(f"Unexpected session heading: {path}")
            c_rows, o_rows, e_rows = parse_text(text, session, year)
            if not o_rows or not any(row["max_raw"] for row in c_rows):
                raise ValueError(f"No threshold tables found: {path}")
            components.extend(c_rows)
            options.extend(o_rows)
            extras.extend(e_rows)
    return components, options, extras


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=Path(os.environ.get("ALEVEL_CS_SOURCES", DEFAULT_SOURCES)))
    parser.add_argument("--output", type=Path, default=ROOT / "corpus/thresholds")
    args = parser.parse_args()
    components, options, extras = extract(args.sources)
    args.output.mkdir(parents=True, exist_ok=True)
    write_csv(args.output / "components.csv", COMPONENT_FIELDS, components)
    write_csv(args.output / "options.csv", OPTION_FIELDS, options)
    write_csv(args.output / "extra_components.csv", COMPONENT_FIELDS, extras)
    print(f"10 PDFs: {len(components)} component rows, {len(options)} options, {len(extras)} extra components")


if __name__ == "__main__":
    main()
