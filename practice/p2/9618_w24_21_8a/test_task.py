import pytest

@pytest.mark.parametrize('mark',range(76))
def test_all_possible_marks(sol,mark):
    """9618_w24_21:8(a) MP1,2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    assert sol.CheckMark(mark) is any(abs(mark-g)<=2 for g in sol.GradeBoundary)

def test_uses_global_boundaries(sol):
    """9618_w24_21:8(a) MP1,2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.GradeBoundary=[70,60,50,40,15]
    assert sol.CheckMark(13) is True
    assert sol.CheckMark(12) is False
    assert sol.CheckMark(72) is True
