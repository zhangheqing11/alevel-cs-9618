from pathlib import Path

ORIGINAL = ["2026-10-01 start", "2026-10-02 run"]


def lines(name):
    return Path(name).read_text(encoding="utf-8").splitlines()


def test_append_existing(sol):
    """B1, B7: append a line without discarding the two existing lines; None return."""
    assert sol.append_entry("log.txt", "2026-10-03 stop") is None
    assert lines("log.txt") == ORIGINAL + ["2026-10-03 stop"]


def test_append_twice(sol):
    """B2, B7: each consecutive append creates its own line."""
    assert sol.append_entry("log.txt", "A") is None
    assert sol.append_entry("log.txt", "B") is None
    assert lines("log.txt") == ORIGINAL + ["A", "B"]


def test_append_new(sol):
    """B3, B7: append mode creates a missing file."""
    assert not Path("new.txt").exists()
    assert sol.append_entry("new.txt", "first") is None
    assert lines("new.txt") == ["first"]


def test_report(sol):
    """B4, B7: overwrite old report, format integer fields, return None."""
    assert sol.write_report("report.txt", ["Ann", "Bo"], [71, 64]) is None
    assert lines("report.txt") == ["Name,Mark", "Ann,71", "Bo,64"]


def test_empty_report(sol):
    """B5, B7: overwrite with only the heading when there are no students."""
    assert sol.write_report("report.txt", [], []) is None
    assert lines("report.txt") == ["Name,Mark"]


def test_report_twice(sol):
    """B6, B7: a second report replaces the first report completely."""
    assert sol.write_report("report.txt", ["Ann"], [71]) is None
    assert sol.write_report("report.txt", ["Bo"], [64]) is None
    assert lines("report.txt") == ["Name,Mark", "Bo,64"]
