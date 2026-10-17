import pytest

@pytest.mark.parametrize('n,expected',[(120,5),(12,-1),(6,3),(1,1),(2,2),(24,4),(25,-1),(5040,7)])
def test_factorial_base(sol,n,expected):
    """9618_w22_22:6(a) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    result=sol.FindBaseNumber(n)
    assert type(result) is int and result==expected
