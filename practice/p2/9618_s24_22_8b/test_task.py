import pytest

@pytest.mark.parametrize('line,expected',[('   IF X2 > 13 THEN','IF X2 > 13 THEN'),(' abc  def ','abc  def '),('abc','abc'),('',''),('   ','')])
def test_leading_spaces_only(sol,line,expected):
    """9618_s24_22:8(b) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    assert sol.DeleteSpaces(line)==expected
