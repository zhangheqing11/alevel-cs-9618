import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('count,new',[(0,800),(3,2),(499,800),(500,800)])
def test_first_unused_pair_sort_and_remaining(sol,candidate_path,monkeypatch,count,new):
    """9618_w22_23:7(b)(i) MP1,2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.ErrCode=list(range(1,count+1))+[999]*(500-count)
    sol.ErrText=['E'+str(i) for i in range(1,count+1)]+['UNDEFINED']*(500-count)
    # For the small case choose a non-existing number between two values.
    if count==3:
        sol.ErrCode[:3]=[1,3,5]
        sol.ErrText[:3]=['E1','E3','E5']
    original=list(zip(sol.ErrCode,sol.ErrText))
    calls=[]
    provided=sol.SortArrays
    def sort():
        calls.append((sol.ErrCode[count],sol.ErrText[count]))
        provided()
    monkeypatch.setattr(sol,'SortArrays',sort)
    result=sol.AddError(new,'new description')
    if count==500:
        assert result==-1 and calls==[]
        assert list(zip(sol.ErrCode,sol.ErrText))==original
    else:
        assert result==499-count and calls==[(new,'new description')]
        assert list(zip(sol.ErrCode,sol.ErrText))[:count+1]==sorted(original[:count]+[(new,'new description')])
        assert sol.ErrCode[count+1:]==[999]*(499-count)
