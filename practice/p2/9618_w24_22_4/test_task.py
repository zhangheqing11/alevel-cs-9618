import pytest

@pytest.mark.parametrize('mins,secs,start',[(5,45,17000),(1,0,0),(2,1,999000)])
def test_warning_and_expiry_use_milliseconds(sol,monkeypatch,mins,secs,start):
    """9618_w24_22:4 MP2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    clock={'next':start,'now':start,'reads':0}
    def read():
        clock['reads']+=1
        assert clock['reads']<1000, 'timer must terminate using the supplied clock'
        value=clock['next']
        clock['now']=value
        clock['next']+=1000
        return value
    messages=[]
    def output(*args,**kwargs):
        messages.append((clock['now'],' '.join(map(str,args))))
    monkeypatch.setattr(sol,'ReadTick',read)
    monkeypatch.setattr('builtins.print',output)
    sol.Timer(mins,secs)
    end=start+1000*(mins*60+secs)
    assert len(messages)==2
    assert end-30000<=messages[0][0]<=end-29000
    assert end<=messages[1][0]<=end+1000
    assert all(text.strip() for _,text in messages)
