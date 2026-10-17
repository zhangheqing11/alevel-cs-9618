import pytest

@pytest.mark.parametrize('s,a,b,expected',[('banana','a','o','bonono'),('Abba','b','X','AXXa'),('ABC','a','x','ABC'),('aaa','a','z','zzz'),('','a','z','')])
def test_replace_all(sol,s,a,b,expected):
    """9618_s23_21:4 MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    assert sol.Replace(s,a,b)==expected
