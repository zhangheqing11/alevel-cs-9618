import pytest
from testkit import feed_input,output_lines
@pytest.mark.parametrize("a,o,b,e",[("7","+","5","Result: 12"),("7","-","10","Result: -3"),("6","*","7","Result: 42"),("7","/","2","Result: 3.5"),("6","/","3","Result: 2.0"),("17","%","5","Result: 2"),("5","/","0","Error: division by zero"),("5","%","0","Error: division by zero"),("5","^","2","Error: unknown operator")])
def test_calc(sol,monkeypatch,capsys,a,o,b,e): """B1-B9: operators, real division, MOD and errors."""; feed_input(monkeypatch,a,o,b); sol.calculator(); assert output_lines(capsys.readouterr().out)==[e]
