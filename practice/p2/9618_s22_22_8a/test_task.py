import pytest

@pytest.mark.parametrize('s,c,expected',[('Abc','A',True),('Abc','a',False),('Abc','c',True),('abc','x',False),('','a',False)])
def test_exists(sol,s,c,expected):
    """9618_s22_22:8(a) MP1,2,3,4,5 (behaviour; syntax/declarations checked manually)."""
    assert sol.Exists(s,c) is expected
