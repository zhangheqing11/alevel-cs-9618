import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

def test_closed_interval_exactly_100_inputs(sol, monkeypatch, capsys):
    """9618_w23_21:2(a) MP1–MP6: both QP endpoints, exclusions, input #100."""
    inputs = [29,30,70,71]+[0]*95+[50]
    feed_input(monkeypatch,*(str(v) for v in inputs))
    sol.main()
    lines = output_lines(capsys.readouterr().out)
    assert len(lines) == 1 and float(lines[0]) == 150


def test_nothing_qualifies(sol, monkeypatch, capsys):
    """9618_w23_21:2(a) MP1,MP3,MP6: initialise zero, final output only."""
    feed_input(monkeypatch,*(["10"]*100))
    sol.main()
    lines = output_lines(capsys.readouterr().out)
    assert len(lines) == 1 and float(lines[0]) == 0
