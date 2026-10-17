import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("search,expected", [("07", ["AB", "fox"]), ("03", ["CD", "owl"]), ("99", [])])
def test_first_match_or_eof(sol, tmp_path, monkeypatch, capsys, search, expected):
    """9618_s22_21:5 MP1–MP8: exact fields, first match, EOF and close."""
    monkeypatch.chdir(tmp_path)
    data = "AB07fox\nCD03owl\nEF07cat\n"
    Path("fields.txt").write_text(data)
    handles = watch_open(monkeypatch)
    sol.main("fields.txt", search, 2, 2, 3)
    assert capsys.readouterr().out.splitlines() == expected
    assert handles and all(h.closed for h in handles)
    assert Path("fields.txt").read_text() == data


def test_other_field_widths(sol, tmp_path, monkeypatch, capsys):
    """9618_s22_21:5 MP4–MP7: use supplied widths, not fixture-specific offsets."""
    monkeypatch.chdir(tmp_path)
    Path("wide.txt").write_text("ABC123tail\nXYZ456last")
    sol.main("wide.txt", "456", 3, 3, 4)
    assert capsys.readouterr().out.splitlines() == ["XYZ", "last"]
