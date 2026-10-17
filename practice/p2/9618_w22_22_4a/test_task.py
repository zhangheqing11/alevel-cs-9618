import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("average,last,expected", [(10,[5,20,10],40),(0,[-1,-2,-3],0),(2.5,[1,4,3],9.5)])
def test_flowchart_data_and_module_trace(sol, monkeypatch, average, last, expected):
    """9618_w22_22:4(a) MP1–MP6: read 4..6, both branches, one final Update."""
    feed_input(monkeypatch,"u-17")
    sol.SameMonth = [999,999,999]+last+[999]
    events = []
    def get(user):
        events.append(("average",user))
        return average
    monkeypatch.setattr(sol,"GetAverage",get)
    monkeypatch.setattr(sol,"Update",lambda user,total: events.append(("update",user,total)))
    sol.main()
    assert events == [("average","u-17"),("update","u-17",expected)]


def test_requested_comparisons(candidate_path):
    """9618_w22_22:4(a) MP5,MP6: D10 asks for the algorithm, not max/sort shortcuts."""
    no_shortcuts(candidate_path)
