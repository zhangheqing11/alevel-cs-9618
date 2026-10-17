import pytest

@pytest.mark.parametrize('number,expected',[('1234567890','******7890'),('1234567897652','*********7652'),('1234567890123456','************3456'),('00000000000000000001','****************0001')])
def test_card_examples_and_bounds(sol,number,expected):
    """9618_w24_22:2(a) MP3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    assert sol.Conceal(number)==expected
