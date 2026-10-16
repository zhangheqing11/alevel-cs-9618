from __future__ import annotations

import json
from pathlib import Path

import pytest

from build.build import build_component, build_ladder, main
from build.stats import calculate_stats, load_rows


FIXTURE = Path(__file__).parent / "fixtures"


def test_stats_counts_and_star_cutoffs():
    rows = load_rows(FIXTURE, 1)
    taxonomy = json.loads((FIXTURE / "papers/p1/taxonomy.json").read_text(encoding="utf-8"))
    stats = calculate_stats(rows, taxonomy["types"])
    db = stats["P1-DB-01"]
    assert db["questions"] == 3
    assert db["marks"] == 6
    assert db["paper_count"] == 2
    assert db["session_count"] == 2
    assert db["cross_questions"] == 0
    assert db["extension_questions"] == 1
    assert db["command_distribution"] == {"explain": 1, "state": 2}
    assert stats["P1-AL-01"]["cross_questions"] == 1
    assert db["score"] == 12
    assert all(item["star"] in (1, 2, 3) for item in stats.values())


def test_fixture_build_replaces_blocks_and_writes_index(tmp_path: Path):
    assert build_component(FIXTURE, tmp_path, 1)
    handbook = (tmp_path / "p1/P1题型手册.md").read_text(encoding="utf-8")
    assert "<!-- auto:" not in handbook
    assert "s24/11 Q1" in handbook
    assert "2021 扩展" in handbook
    assert "a unique identifier" in handbook
    html = (tmp_path / "p1/P1题型手册.html").read_text(encoding="utf-8")
    assert "9618_s24_qp_11.pdf p.2" in html
    assert "class=\"score-sentence\"" in html
    assert "codehilite" in html
    assert "PingFang SC" in html
    index = json.loads((tmp_path / "p1/index.json").read_text(encoding="utf-8"))
    assert set(index["types"]) == {"P1-DB-01", "P1-AL-01"}
    db = index["types"]["P1-DB-01"]
    assert db["representative"]["id"] == "9618_s24_11:1"
    assert db["next_variation"]["id"] == "9618_w23_12:1"
    assert db["exercise_paths"] == ["practice/p1/db-ex1"]
    assert db["drills"][0]["id"] == "9618_s24_11:1"


def test_ladder_build_and_missing_inputs_are_graceful(tmp_path: Path):
    assert build_ladder(FIXTURE, tmp_path)
    assert (tmp_path / "ladder/Python阶梯.html").exists()
    ladder_index = json.loads((tmp_path / "ladder/index.json").read_text(encoding="utf-8"))
    assert ladder_index["levels"][0]["id"] == "L01-basics"
    missing = tmp_path / "missing"
    missing.mkdir()
    assert main(["all", "--root", str(missing), "--out", str(tmp_path / "out")]) == 0


@pytest.mark.parametrize("command", ["p1", "p2", "p3", "p4"])
def test_component_command_without_taxonomy_does_not_fail(tmp_path: Path, command: str):
    assert main([command, "--root", str(tmp_path), "--out", str(tmp_path / "out")]) == 0
