import pytest,re

@pytest.mark.parametrize('s,total,average',[('12,13,451,22',498,124.5),('9',9,9),('0,10,2',12,4),('1,2',3,1.5)])
def test_total_average(sol,capsys,s,total,average):
    """9618_s22_22:6 MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    sol.Parse(s)
    out=capsys.readouterr().out
    nums=re.findall(r'-?\d+(?:\.\d+)?',out)
    assert [float(n) for n in nums] == [total,average]
    assert any(c.isalpha() for c in out)
