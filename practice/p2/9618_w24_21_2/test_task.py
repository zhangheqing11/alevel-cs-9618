import pytest
from collections import Counter

@pytest.mark.parametrize('start,end,alarms,days',[((16,30,10),(16,30,11),0,0),((16,30,59),(16,31,0),1,0),((16,59,59),(17,0,0),1,0),((23,59,59),(0,0,0),1,1),((0,0,0),(0,0,1),0,0)])
def test_clock_rollovers_and_callbacks(sol,monkeypatch,start,end,alarms,days):
    """9618_w24_21:2 MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    sol.HH,sol.MM,sol.SS=start
    calls=[]
    def alarm():
        assert sol.SS==0
        calls.append('alarm')
    def day():
        assert (sol.HH,sol.MM,sol.SS)==(0,0,0)
        calls.append('day')
    monkeypatch.setattr(sol,'CheckAlarm',alarm)
    monkeypatch.setattr(sol,'NewDay',day)
    sol.Tick()
    assert (sol.HH,sol.MM,sol.SS)==end
    assert Counter(calls)==Counter({'alarm':alarms,'day':days})
