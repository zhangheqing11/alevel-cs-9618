import pytest,re
from testkit import feed_input

@pytest.mark.parametrize('inputs,a,b',[(('1.5','2.5','0','8','0'),4,8),(('0','0'),0,0),(('-2','0','6','0'),-2,6)])
def test_two_parts(sol,monkeypatch,capsys,inputs,a,b):
    """9618_s24_23:4(a) MP3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    sol.TotalA=100
    sol.TotalB=100
    feed_input(monkeypatch,*inputs)
    sol.TwoParts()
    assert sol.TotalA==a and sol.TotalB==b
    out=capsys.readouterr().out
    assert float(re.findall(r'-?\d+(?:\.\d+)?',out)[-1])==(a+b)/2
    assert any(c.isalpha() for c in out)
