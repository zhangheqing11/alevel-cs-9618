import pytest
from testkit import feed_input,output_lines
@pytest.mark.parametrize("v,e,m",[(("72",),72,[]),(("105","-3","72"),72,["Invalid: must be 0 to 100"]*2),(("0",),0,[]),(("100",),100,[]),(("101","100"),100,["Invalid: must be 0 to 100"]),(("-1","0"),0,["Invalid: must be 0 to 100"])])
def test_mark(sol,monkeypatch,capsys,v,e,m): """B1-B7: validation, inclusive edges, messages and int return."""; feed_input(monkeypatch,*v); r=sol.get_mark(); assert r==e and type(r) is int and output_lines(capsys.readouterr().out)==m
