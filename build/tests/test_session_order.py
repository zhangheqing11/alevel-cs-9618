from __future__ import annotations

import importlib.util
from pathlib import Path

from build.stats import rows_for_type


ROWS_SCRIPT = Path(__file__).parents[2] / "skill/cie-9618-cs-tutor/scripts/rows.py"


def _rows_module():
    spec = importlib.util.spec_from_file_location("tutor_rows", ROWS_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _same_year_rows() -> list[dict]:
    return [
        {
            "id": "9618_s24_11:1",
            "paper": "9618_s24_11",
            "session": "s",
            "year": 2024,
            "variant": 1,
            "q": "1",
            "qn": 1,
            "types": {"primary": "P1-DB-01", "cross": []},
        },
        {
            "id": "9618_w24_11:1",
            "paper": "9618_w24_11",
            "session": "w",
            "year": 2024,
            "variant": 1,
            "q": "1",
            "qn": 1,
            "types": {"primary": "P1-DB-01", "cross": []},
        },
    ]


def test_same_year_w_session_is_newer_in_stats_and_drills():
    rows = _same_year_rows()

    stats_order = [row["paper"] for row in rows_for_type(rows, "P1-DB-01")]
    assert stats_order == ["9618_w24_11", "9618_s24_11"]

    tutor_rows = _rows_module()
    drills_order = [row["paper"] for row in sorted(rows, key=tutor_rows.newest_first)]
    assert drills_order == ["9618_w24_11", "9618_s24_11"]
