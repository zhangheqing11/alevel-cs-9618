import pytest

@pytest.mark.parametrize('n,c,expected',[(3,'Z','ZZZ'),(1,'!','!'),(0,'x','ERROR'),(-3,'x','ERROR'),(5,' ','     ')])
def test_make_string(sol,n,c,expected):
    """9618_s23_23:4 MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    assert sol.MakeString(n,c)==expected
