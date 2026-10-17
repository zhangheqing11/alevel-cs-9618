import pytest

@pytest.mark.parametrize('n,expected',[(-5,-1),(0,1),(1,1),(5,120),(7,5040)])
def test_factorial(sol,n,expected):
    """9618_s22_23:6(a) MP2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    value=sol.Factorial(n)
    assert type(value) is int and value == expected
