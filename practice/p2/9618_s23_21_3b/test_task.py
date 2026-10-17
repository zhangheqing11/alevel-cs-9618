import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("amount,expected", [("0",0),("9.99",45),("10",70),("99.77",693),("100",700),("100.99",1000),("101",1010)])
def test_whole_dollars_and_bands(sol, monkeypatch, capsys, amount, expected):
    """9618_s23_21:3(b) MP1–MP6: QP sample, both thresholds, whole dollar calculation."""
    feed_input(monkeypatch, amount)
    sol.main()
    lines = output_lines(capsys.readouterr().out)
    assert len(lines) == 1 and float(lines[0]) == expected
