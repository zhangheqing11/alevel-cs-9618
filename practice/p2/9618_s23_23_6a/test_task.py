import pytest
from testkit import output_lines

@pytest.mark.parametrize('start,end',[(15,61),(141,143),(100,150),(60,61),(999,1061)])
def test_exclusive_range(sol,capsys,start,end):
    """9618_s23_23:6(a) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    sol.Select(start,end)
    expected=[str(n) for n in range(start+1,end) if n%10+(n//10)%10==6]
    assert output_lines(capsys.readouterr().out)==expected
