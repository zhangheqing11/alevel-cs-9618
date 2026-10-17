import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

from datetime import date

@pytest.mark.parametrize("day,name", [(18,"Sunday"),(19,"Monday"),(20,"Tuesday"),(21,"Wednesday"),(22,"Thursday"),(23,"Friday"),(24,"Saturday")])
def test_all_weekdays(sol, capsys, day, name):
    """9618_s23_22:2(c) MP3–MP6 (MS Steps 1–4): QP Thursday sample and array endpoints."""
    sol.MyDOB = date(2023,6,day)
    sol.main()
    assert output_lines(capsys.readouterr().out) == [name]
