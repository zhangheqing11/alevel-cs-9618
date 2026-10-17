from collections import Counter
import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('mode',['mixed','descending','sorted','equal'])
def test_sort_full_array_keeps_sensor_pairs(sol,candidate_path,mode):
    """9618_s25_21:6(b) MP2,3,4,5,7,8,9; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    speeds=[(i*37)%61 for i in range(2000)]
    if mode=='descending':
        speeds=sorted(speeds,reverse=True)
    if mode=='sorted':
        speeds=sorted(speeds)
    if mode=='equal':
        speeds=[30]*2000
    original=[[speed,(i%50)+1] for i,speed in enumerate(speeds)]
    sol.Reading=[row[:] for row in original]
    sol.Sort()
    assert len(sol.Reading)==2000
    assert [row[0] for row in sol.Reading]==sorted(speeds)
    assert Counter(map(tuple,sol.Reading))==Counter(map(tuple,original))
