import pytest
from testkit import feed_input,output_lines
@pytest.mark.parametrize("b,p,e",[("100","4",["Total: 110.00","Each: 27.50"]),("80","3",["Total: 88.00","Each: 29.33"]),("12.40","1",["Total: 13.64","Each: 13.64"]),("0","5",["Total: 0.00","Each: 0.00"]),("45","2",["Total: 49.50","Each: 24.75"])])
def test_bill(sol,monkeypatch,capsys,b,p,e): """B1-B5: service charge, real input, split and two decimals."""; feed_input(monkeypatch,b,p); sol.split_bill(); assert output_lines(capsys.readouterr().out)==e
