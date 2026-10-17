from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('count,blank,expected',[(0,0,False),(1,0,False),(9,20,False),(10,5,True),(11,0,True)])
def test_nonblank_threshold(candidate_path,exercise_dir,tmp_path,monkeypatch,count,blank,expected):
    """9618_w22_21:8(a) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('project.txt').write_text('\n'*blank+'\n'.join('OUTPUT '+str(i) for i in range(count)))
    handles=watch_open(monkeypatch)
    assert module.CheckFile('project.txt') is expected
    assert handles and all(h.closed for h in handles)
