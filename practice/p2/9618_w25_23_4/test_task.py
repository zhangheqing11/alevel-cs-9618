import pytest

@pytest.mark.parametrize('values',[[101,456,219,754],[101,456,219,754,328],list(range(100,120)),list(range(100,125))])
def test_complete_substrings_and_capacity(sol,values):
    """9618_w25_23:4 MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    sol.NumString=','.join(map(str,values))
    sol.Data=[-1]*20
    sol.Store()
    assert sol.Data[:min(len(values),20)]==values[:20]
    assert len(sol.Data)==20
    assert all(type(v) is int for v in sol.Data[:min(len(values),20)])
