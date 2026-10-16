import pytest
from testkit import feed_input,output_lines
@pytest.mark.parametrize("v,e",[((60,70,85),["Total: 215","Average: 71.7"]),((0,0,0),["Total: 0","Average: 0.0"]),((100,100,99),["Total: 299","Average: 99.7"]),((1,2,2),["Total: 5","Average: 1.7"]),((50,50,51),["Total: 151","Average: 50.3"])])
def test_average(sol,monkeypatch,capsys,v,e): """B1-B5: corrected total, division and one decimal."""; feed_input(monkeypatch,*map(str,v)); sol.mark_summary(); assert output_lines(capsys.readouterr().out)==e
