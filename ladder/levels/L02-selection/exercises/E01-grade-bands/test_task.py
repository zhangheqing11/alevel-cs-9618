import pytest
@pytest.mark.parametrize("m,e",[(85,"A"),(100,"A"),(80,"A"),(79,"B"),(70,"B"),(69,"C"),(60,"C"),(59,"D"),(50,"D"),(49,"E"),(40,"E"),(39,"U"),(0,"U"),(-1,"Invalid"),(101,"Invalid")])
def test_grade(sol,m,e): """B1-B8: every band edge, invalid values and str return."""; assert sol.grade(m)==e and type(sol.grade(m)) is str
