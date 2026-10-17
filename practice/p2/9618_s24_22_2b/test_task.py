import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("flags", [[True],[False,True],[False,False,True]])
def test_flowchart_order_and_ports(sol, monkeypatch, flags):
    """9618_s24_22:2(b) MP1–MP5: trace the QP module calls, terminate before extra reset."""
    values = iter(flags)
    events = []
    def status():
        value = next(values)
        events.append(("GetStat",value))
        return value
    monkeypatch.setattr(sol,"GetStat",status)
    monkeypatch.setattr(sol,"Reset",lambda port: events.append(("Reset",port)))
    sol.main()
    expected = []
    for flag in flags:
        expected.append(("GetStat",flag))
        if not flag:
            expected.extend(("Reset",port) for port in [1,2,3])
    assert events == expected
