import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("inputs,expected", [(["0"],[0,0]),(["1.5","-2.25","3.75","-0.5","0"],[5.25,-2.75]),(["-7","-1","0"],[0,-8]),(["2","4","0"],[6,0])])
def test_two_totals_after_zero(sol, monkeypatch, capsys, inputs, expected):
    """9618_w22_23:3 MP1–MP5: real inputs, zero sentinel, final two sums."""
    feed_input(monkeypatch,*inputs)
    sol.main()
    lines = output_lines(capsys.readouterr().out)
    assert len(lines) == 2
    assert [float(x) for x in lines] == expected
