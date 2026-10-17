import pytest

@pytest.mark.parametrize('s,expected',[('253444',1),('253000',2),('410410',3),('111111',3),('000000',3),('123456',0),('123011',0)])
def test_highest_condition(sol,s,expected):
    """9618_w23_23:6 MP2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    result=sol.TestNum(s)
    assert type(result) is int and result==expected
