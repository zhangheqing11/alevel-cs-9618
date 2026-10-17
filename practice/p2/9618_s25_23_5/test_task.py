import pytest

@pytest.mark.parametrize('s,expected',[('0010010110','00100101100'),('101010','1010101'),('0','00'),('1','11'),('111','1111'),('1111','11110')])
def test_parity_bit(sol,s,expected):
    """9618_s25_23:5 MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    assert sol.Parity(s)==expected
