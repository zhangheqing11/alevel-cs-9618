import pytest

@pytest.mark.parametrize('grades',[[65,57,43,35,27],[70,60,50,40,15],[70,68,50,17,15]])
def test_reset_all_entries_and_inclusive_ranges(sol,grades):
    """9618_w24_23:4(b)(ii) MP2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.GB=grades[:]
    sol.Check=[True]*76
    sol.GBInitialise()
    assert sol.Check==[any(abs(i-g)<=2 for g in grades) for i in range(76)]
    assert all(type(x) is bool for x in sol.Check)
    assert sol.GB==grades
