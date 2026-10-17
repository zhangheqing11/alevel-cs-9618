import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

def test_qp_sample_thresholds_and_last_week(sol, tmp_path, monkeypatch, capsys):
    """9618_s25_23:4(a) MP1–MP6: QP rows, strictly >500, week numbers 1..52."""
    monkeypatch.chdir(tmp_path)
    values = [350,502,434] + [0]*45 + [492,872,772,201]
    values[3],values[4],values[51] = 500,501,999
    text = "\n".join(str(v) for v in values)
    Path("Sales.txt").write_text(text)
    handles = watch_open(monkeypatch)
    sol.main()
    assert output_lines(capsys.readouterr().out) == ["2","5","50","51","52"]
    assert handles and all(h.closed for h in handles)
    assert Path("Sales.txt").read_text() == text


def test_no_week_above_threshold(sol, tmp_path, monkeypatch, capsys):
    """9618_s25_23:4(a) MP3,MP4,MP6: exactly 52 valid records, no qualifying weeks."""
    monkeypatch.chdir(tmp_path)
    Path("Sales.txt").write_text("500\n"*52)
    sol.main()
    assert capsys.readouterr().out == ""
