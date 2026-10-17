import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('dest,expected',[('100',1),('199',1),('200',2),('259',2),('260',2),('283',2),('999',1)])
def test_qp_ranges_including_ends(sol,candidate_path,dest,expected):
    """9618_w23_22:8(a) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    assert sol.GetPort(dest)==expected

def test_gaps_unused_row_and_last_row(sol):
    """9618_w23_22:8(a) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    sol.RouteTable=[[-1,1000,3],[100,150,2],[-1,1000,1],[-1,1000,3],[-1,1000,1],[900,999,3]]
    assert sol.GetPort('100')==2
    assert sol.GetPort('500')==-1
    assert sol.GetPort('999')==3
