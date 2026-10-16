import pytest
E=[1.5,3.,4.2,5.4,10.8,13.2]
def test_predicted(sol): """B1: six dry-run values."""; assert sol.PREDICTED==pytest.approx(E,abs=1e-9)
@pytest.mark.parametrize("w,x,e",[(100,False,1.5),(0,False,1.5),(101,False,3.),(500,False,3.),(501,False,4.2),(750,False,5.4),(1250,False,7.8),(1001,False,6.6),(751,True,10.8),(1000,True,13.2),(100,True,3.)])
def test_postage(sol,w,x,e): """B2-B8: boundaries, DIV, express and float."""; r=sol.postage(w,x); assert r==pytest.approx(e,abs=1e-9) and type(r) is float
