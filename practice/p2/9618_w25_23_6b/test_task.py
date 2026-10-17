import pytest

@pytest.mark.parametrize('number,expected',[(41623,True),(41633,False),(1001,True),(9997,True),(10090,True),(12345678,True),(12345679,False)])
def test_check_digit(sol,number,expected):
    """9618_w25_23:6(b) MP2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    assert sol.CheckNumber(number) is expected
