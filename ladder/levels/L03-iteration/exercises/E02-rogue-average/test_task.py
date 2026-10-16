import pytest
from testkit import feed_input,output_lines
@pytest.mark.parametrize("v,e",[(("5","10","15","-1"),["Count: 3","Total: 30","Average: 10.0"]),(("-1",),["No data"]),(("0","-1"),["Count: 1","Total: 0","Average: 0.0"]),(("-5","5","-1"),["Count: 2","Total: 0","Average: 0.0"]),(("7","8","-1"),["Count: 2","Total: 15","Average: 7.5"]),(("1","2","2","-1"),["Count: 3","Total: 5","Average: 1.7"])])
def test_rogue(sol,monkeypatch,capsys,v,e): """B1-B6: sentinel pre-read, negatives, zero data and format."""; feed_input(monkeypatch,*v); sol.rogue_average(); assert output_lines(capsys.readouterr().out)==e
