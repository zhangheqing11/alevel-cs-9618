import pytest
@pytest.mark.parametrize("y,e",[(2024,True),(2023,False),(1900,False),(2100,False),(2000,True),(2400,True),(4,True),(1,False)])
def test_leap(sol,y,e): """B1-B6: MOD rule, century exceptions and bool return."""; r=sol.is_leap(y); assert r is e and type(r) is bool
