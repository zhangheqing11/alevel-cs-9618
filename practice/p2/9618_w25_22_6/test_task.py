import pytest

@pytest.mark.parametrize('a,b,case,pos,expected',[('Cat','Catalogue',True,'s',True),('CAT','Catalogue',True,'s',False),('CAT','Catalogue',False,'s',True),('Cat','Catalogue',True,'e',False),('GUE','Catalogue',False,'e',True),('Catalogue','Cat',True,'s',False),('abc','abc',True,'e',True),('','abc',False,'e',True)])
def test_qp_comparisons(sol,a,b,case,pos,expected):
    """9618_w25_22:6 MP2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    assert sol.Compare(a,b,case,pos) is expected
