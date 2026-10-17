import pytest

@pytest.mark.parametrize('odd,even,last,expected',[(3,2,2,'Odd'),(2,3,3,'Even'),(4,4,4,'Same'),(-3,-2,-2,'Even'),(0,0,1,'Even')])
def test_qp_index_parity_and_last_element(sol,odd,even,last,expected):
    """9618_s24_21:4 MP3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.Data=[odd if i%2==0 else even for i in range(100)]
    sol.Data[99]=last
    before=sol.Data[:]
    assert sol.Check()==expected
    assert sol.Data==before
