"""Source-backed checks; run with the shared alevel-cs environment."""
import csv
import importlib.util
import random
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location("extract_gt", Path(__file__).with_name("extract_gt.py"))
gt = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gt)
ROOT = Path(__file__).resolve().parents[2]


def read_csv(name):
    path = ROOT / "corpus/thresholds" / name
    assert path.read_bytes().startswith(b"\xef\xbb\xbf")
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def test_old_format_preserves_dash_and_missing_components():
    text = """The maximum total mark for this syllabus, after weighting has been applied, is 300 for A Level and 150 for
AS Level.
Component 11  75  45  40  34  28  22
AX  11, 21, 31, 41  213  186  159  131  103  75
SX  11, 21  –  86  74  62  50  38
"""
    components, options, extras = gt.parse_text(text, "s", 2021)
    assert len(components) == 12
    assert components[0]["A"] == "45"
    assert components[-1]["max_raw"] == ""
    assert options[0]["max_weighted"] == "300"
    assert options[1]["A*"] == "–"
    assert options[1]["max_weighted"] == "150"
    assert extras == []


def test_explicit_maximum_and_unusual_options_are_preserved():
    text = """Component 50  75  51  42  33  24  15
2W  300  11, 22, 32, 42  233  198  163  132  101  70
BYJ  150  32, 42  129  108  87  65  44  23
P1  75  50  –  51  42  33  24  15
"""
    _, options, extras = gt.parse_text(text, "s", 2022)
    assert [row["option"] for row in options] == ["2W", "BYJ", "P1"]
    assert options[0]["components"] == "11;22;32;42"
    assert options[1]["A*"] == "129"
    assert extras[0]["component"] == "50"


@pytest.mark.parametrize("line", ["Component 11  75  45  40", "AX  300  11, 21  50  40", "AX  300  11, 21  90  80  70  x  50  40"])
def test_malformed_rows_are_rejected(line):
    with pytest.raises(ValueError):
        gt.parse_text(line, "s", 2024)


def test_2021_a2_only_maximum_is_unknown_not_invented():
    text = """The maximum total mark is 300 for A Level and 150 for AS Level.
BQJ  31, 41  114  97  80  64  48  33
"""
    _, options, _ = gt.parse_text(text, "w", 2021)
    assert options[0]["max_weighted"] == ""


@pytest.fixture(scope="module")
def tables():
    return read_csv("components.csv"), read_csv("options.csv"), read_csv("extra_components.csv")


@pytest.fixture(scope="module")
def source_rows():
    # Independent PDF engine and whitespace tokenisation, not the extractor's
    # Poppler output or its regular expressions. Keep page numbers for failures.
    import os
    import pymupdf

    source_dir = Path(os.environ.get("ALEVEL_CS_SOURCES", gt.DEFAULT_SOURCES)) / "pastpapers"
    sources = {}
    for year in range(2021, 2026):
        for session in ("s", "w"):
            path = source_dir / f"9618_{session}{year % 100:02}_gt.pdf"
            components, options = {}, {}
            with pymupdf.open(path) as document:
                for page_no, page in enumerate(document, 1):
                    for line in page.get_text(sort=True).splitlines():
                        tokens = line.split()
                        if tokens[:1] == ["Component"] and len(tokens) == 8:
                            components[tokens[1]] = (tokens[2:], page_no)
                        elif tokens and 2 <= len(tokens[0]) <= 3 and tokens[0].isalnum() and tokens[0].upper() == tokens[0]:
                            if len(tokens) < 8 or not tokens[-1].isdigit():
                                continue
                            code = tokens[0]
                            maximum = tokens[1] if year != 2021 else None
                            combo = "".join(tokens[2:-6] if year != 2021 else tokens[1:-6]).replace(",", ";")
                            options[code] = (maximum, combo, tokens[-6:], page_no)
            sources[session, str(year)] = components, options
    return sources


EXPECTED_COUNTS = {
    ("s", "2021"): (12, 6, 0), ("w", "2021"): (10, 11, 0),
    ("s", "2022"): (12, 22, 2), ("w", "2022"): (12, 23, 1),
    ("s", "2023"): (12, 15, 2), ("w", "2023"): (12, 17, 1),
    ("s", "2024"): (12, 12, 0), ("w", "2024"): (12, 18, 0),
    ("s", "2025"): (12, 15, 2), ("w", "2025"): (12, 17, 0),
}


@pytest.mark.parametrize("key", EXPECTED_COUNTS)
def test_every_printed_cell_and_table_count(key, tables, source_rows):
    components, options, extras = [[r for r in rows if (r["session"], r["year"]) == key] for rows in tables]
    printed_components, printed_options = source_rows[key]
    count, option_count, extra_count = EXPECTED_COUNTS[key]
    assert len(components) == 12
    assert len(options) == option_count == len(printed_options)
    assert len(extras) == extra_count
    assert len(printed_components) == count + extra_count
    assert {r["component"] for r in components} == set(gt.COMPONENTS)
    assert {r["option"] for r in options} == set(printed_options)
    assert len({r["component"] for r in components + extras}) == len(components + extras)
    for row in components + extras:
        values = [row[field] for field in gt.COMPONENT_FIELDS[3:]]
        if row["component"] not in printed_components:
            assert key == ("w", "2021") and row["component"] in {"33", "43"}
            assert values == [""] * 6
        else:
            expected, page = printed_components[row["component"]]
            assert values == expected, (key, page, row)
            assert row["max_raw"] == "75"
    for row in options:
        maximum, combo, grades, page = printed_options[row["option"]]
        assert row["components"] == combo, (key, page, row)
        assert [row[field] for field in gt.OPTION_FIELDS[5:]] == grades, (key, page, row)
        if maximum is not None:
            assert row["max_weighted"] == maximum, (key, page, row)
        elif row["option"].endswith("J"):
            assert row["max_weighted"] == ""
        else:
            assert row["max_weighted"] == ("150" if row["option"].startswith("S") else "300")
        if len(combo.split(";")) == 4:
            assert row["max_weighted"] == "300"
        if row["option"] in {"SX", "SY", "SZ"}:
            assert row["max_weighted"] == "150"
            assert row["A*"] == "–"


@pytest.mark.parametrize("key", EXPECTED_COUNTS)
def test_three_random_cells_per_pdf(key, tables, source_rows):
    rng = random.Random(f"T40-{key[0]}{key[1]}")
    candidates = []
    for rows, printed, id_field, fields in [
        (tables[0] + tables[2], source_rows[key][0], "component", gt.COMPONENT_FIELDS[3:]),
        (tables[1], source_rows[key][1], "option", gt.OPTION_FIELDS[5:]),
    ]:
        for row in rows:
            if (row["session"], row["year"]) != key or row[id_field] not in printed:
                continue
            values = printed[row[id_field]][0 if id_field == "component" else 2]
            candidates.extend((row, field, expected) for field, expected in zip(fields, values))
    for row, field, expected in rng.sample(candidates, 3):
        assert row[field] == expected, (key, row, field)


def test_full_counts_and_reproducible_csv(tables, tmp_path):
    assert [len(table) for table in tables] == [120, 156, 8]
    generated = gt.extract(Path(__import__("os").environ.get("ALEVEL_CS_SOURCES", gt.DEFAULT_SOURCES)))
    for name, fields, rows in zip(["components.csv", "options.csv", "extra_components.csv"],
                                  [gt.COMPONENT_FIELDS, gt.OPTION_FIELDS, gt.COMPONENT_FIELDS], generated):
        gt.write_csv(tmp_path / name, fields, rows)
        assert (tmp_path / name).read_bytes() == (ROOT / "corpus/thresholds" / name).read_bytes()
