import pytest
from testkit import feed_input,output_lines
@pytest.mark.parametrize("v,e",[(("50","10"),["Due: 10","Change: 0"]),(("20","20","50"),["Due: 40","Due: 20","Change: 30"]),(("5","50","1","20"),["Rejected: 5","Due: 60","Due: 10","Rejected: 1","Due: 10","Change: 10"]),(("50","50"),["Due: 10","Change: 40"]),(("10","10","10","10","10","10"),["Due: 50","Due: 40","Due: 30","Due: 20","Due: 10","Change: 0"]),(("20","20","20"),["Due: 40","Due: 20","Change: 0"])])
def test_coins(sol,monkeypatch,capsys,v,e): """B1-B6: accepted/rejected coins, Due and Change."""; feed_input(monkeypatch,*v); sol.coin_machine(); assert output_lines(capsys.readouterr().out)==e
