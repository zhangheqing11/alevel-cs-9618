import pytest

@pytest.mark.parametrize('switch,expected',[(1,'a'),(2,'y'),(3,'7'),(0,'*'),(-1,'*'),(4,'*')])
def test_switch_assignments(sol,switch,expected):
    """9618_s22_21:6(b) MP1,2,3,4 (behaviour; syntax/declarations checked manually)."""
    sol.MySwitch = switch
    sol.main()
    assert sol.ThisChar == expected
