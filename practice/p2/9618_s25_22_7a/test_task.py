import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('count,target,expected',[(0,10001,-1),(1,10001,0),(501,10501,1500),(1000,11000,2997),(3,10004,-1),(3,10000,-1),(3,11001,-1),(3,99999,-1)])
def test_found_missing_range_full_boundary(sol,candidate_path,count,target,expected):
    """9618_s25_22:7(a) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Loyalty=[[10001+i,i*3] if i<count else [99999,777] for i in range(1000)]
    before=[r[:] for r in sol.Loyalty]
    assert sol.FindCustomer(target)==expected
    assert sol.Loyalty==before
