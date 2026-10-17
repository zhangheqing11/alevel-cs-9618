import pytest

@pytest.mark.parametrize('coords,expected',[((0,0,3,0,0,4),True),((3,0,0,0,0,4),True),((0,0,0,4,3,0),True),((3,2,6,6,8,3),False),((-2,-1,-2,2,2,-1),True)])
def test_coordinate_triangles(sol,coords,expected):
    """9618_s24_21:6(a) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    assert sol.IsRA(*coords) is expected
