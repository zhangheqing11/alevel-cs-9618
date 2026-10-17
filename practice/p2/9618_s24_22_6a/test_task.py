import pytest

@pytest.mark.parametrize('name,expected',[('Bat out of Hull','Bat out of Hull'),('Bohemian Symphony','Bohemian...'),('Paperbook Writer','Paperbook Writer'),('Chris Sings the Blues','Chris Sings...'),('Green Home Alabama','Green Home...'),('abcdefghijklm longword','abcdefghijklm...'),('A abcdefghijklmn','A abcdefghijklmn'),('A abcdefghijkl longer','A...'),('A abcdefghijklmnp','A...')])
def test_title_examples_and_limits(sol,name,expected):
    """9618_s24_22:6(a) MP2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    assert sol.Trim(name)==expected
