import pytest

@pytest.mark.parametrize('s,expected',[('Racecar',True),('madam',True),('12344321',True),('Ab',False),('abca',False),('a',True),('AA',True)])
def test_palindromes(sol,s,expected):
    """9618_s22_21:7(a) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    assert sol.IsPalindrome(s) is expected
