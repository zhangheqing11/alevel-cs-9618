import pytest

@pytest.mark.parametrize('sid,desc,cost',[('12345','A'*32,'12.30'),('00001','A description'.ljust(32),'0'),('99999',' '*32,'123456.78')])
def test_all_byref_fields(sol,sid,desc,cost):
    """9618_w22_23:5(a)(i) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    a,b,c=['old'],['old'],['old']
    sol.Unpack(sid+desc+cost,a,b,c)
    assert (a[0],b[0],c[0])==(sid,desc,cost)
