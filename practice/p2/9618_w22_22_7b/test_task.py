import pytest
from collections import Counter
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('codes',[[60,10,50,20],list(range(500,0,-1)),[10,20,50,60],[]])
def test_bubble_pairs_unused_tail_and_full(sol,candidate_path,codes):
    """9618_w22_22:7(b) MP2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.ErrCode=codes+[999]*(500-len(codes))
    sol.ErrText=['E'+str(c) for c in codes]+['UNDEFINED']*(500-len(codes))
    pairs=Counter(zip(sol.ErrCode,sol.ErrText))
    sol.SortArrays()
    assert sol.ErrCode==sorted(codes)+[999]*(500-len(codes))
    assert Counter(zip(sol.ErrCode,sol.ErrText))==pairs
