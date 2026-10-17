import pytest

@pytest.mark.parametrize('s,start,n,expected',[('Cambridge',1,3,'Cam'),('Cambridge',4,3,'bri'),('Cambridge',9,1,'e'),('abc',1,3,'abc'),('abc',2,1,'b')])
def test_mid_positions(sol,s,start,n,expected):
    """9618_s22_22:7(a) MP1,2,3,4 (behaviour; syntax/declarations checked manually)."""
    assert sol.MID(s,start,n)==expected
