import re,pytest

@pytest.mark.parametrize('number,points,left,free',[(16,9,3,2),(1,10,0,1),(1,9,10,0),(22,0,0,2),(2,9,0,1)])
def test_coffee_points(sol,capsys,number,points,left,free):
    """9618_s25_21:7(a) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    result=sol.CustomerOrder(number,points)
    assert type(result) is int and result==left
    message=capsys.readouterr().out
    assert [int(x) for x in re.findall(r'\d+',message)]==[free]
    assert any(c.isalpha() for c in message)
