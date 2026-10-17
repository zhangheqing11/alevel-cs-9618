import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('positions,limit,expected',[([],0,False),([0],1,False),([0,149],1,True),([149],0,True),(list(range(150)),149,True)])
def test_exact_count_strict_threshold_and_last(sol,candidate_path,positions,limit,expected):
    """9618_w23_21:4(a) MP3,4,5,6; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Data=['Target extra']*150
    for p in positions:
        sol.Data[p]='Target'
    assert sol.TooMany('Target',limit) is expected
