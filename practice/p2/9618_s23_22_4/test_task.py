import pytest

@pytest.mark.parametrize('s,c,expected',[('banana','a',3),('AaAa','a',2),('xyz','z',1),('abc','x',0),('','x',0)])
def test_character_count(sol,s,c,expected):
    """9618_s23_22:4 MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    value=sol.GetNum(s,c)
    assert type(value) is int and value==expected
