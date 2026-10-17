import pytest
from testkit import output_lines

@pytest.mark.parametrize('dim',range(1,10))
def test_all_number_squares(sol,capsys,dim):
    """9618_s23_22:6 MP2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    sol.Square(dim)
    border=str(dim)*dim
    expected=[border] if dim==1 else [border]+[str(dim)+'*'*(dim-2)+str(dim)]*(dim-2)+[border]
    assert output_lines(capsys.readouterr().out)==expected
