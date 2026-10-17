import pytest

@pytest.mark.parametrize('s,expected',[('0001Abc'+'x'*12,True),('5999XYZ'+'long description',True),('0000ABC'+'x'*12,False),('6000ABC'+'x'*12,False),('0001A1C'+'x'*12,False),('00x1ABC'+'x'*12,False),('0001ABC'+'x'*11,False),('',False)])
def test_stock_line(sol,s,expected):
    """9618_s23_22:8(a) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    assert sol.CheckInfo(s) is expected

def test_uses_supplied_alpha_contract(sol,monkeypatch):
    """9618_s23_22:8(a) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    monkeypatch.setattr(sol,'OnlyAlpha',lambda s:False)
    assert sol.CheckInfo('0001ABC'+'x'*12) is False
