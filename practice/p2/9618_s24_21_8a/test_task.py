import pytest

@pytest.mark.parametrize('line,expected',[('IF X2 > 13 THEN    //check if limit exceeded','IF X2 > 13 THEN    '),('X //first //second','X '),('//only comment',''),('a/b','a/b'),('abc//','abc'),('',''),('/','/')])
def test_comment_boundary(sol,line,expected):
    """9618_s24_21:8(a) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    assert sol.DeleteComment(line)==expected
