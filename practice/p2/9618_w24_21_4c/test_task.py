import pytest

@pytest.mark.parametrize('x,y,done,value',[('10','4',True,2.5),('-3','2',True,-1.5),('0','2',True,0),('5.5','0.5',True,11),('abc','2',False,None),('2','abc',False,None),('2','0',False,None),('2','0.0',False,None)])
def test_result_record(sol,x,y,done,value):
    """9618_w24_21:4(c) MP2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    result=sol.Evaluate(x,y)
    assert result.Done is done
    if done:
        assert type(result.Value) in (int,float) and result.Value==pytest.approx(value)
