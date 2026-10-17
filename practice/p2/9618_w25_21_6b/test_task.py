import pytest

@pytest.mark.parametrize('number,expected',[(4162,41623),(100,1001),(999,9997),(1009,10090),(1234567,12345678)])
def test_generate_digit(sol,number,expected):
    """9618_w25_21:6(b) MP2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    result=sol.Generate(number)
    assert type(result) is int and result==expected
