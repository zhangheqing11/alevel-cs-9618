from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('count',[1,3,10,100,999])
def test_suffix_and_exact_single_line(candidate_path,exercise_dir,tmp_path,monkeypatch,count):
    """9618_w23_22:6(a) MP2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('TestData.001').write_text('obsolete data\nsecond line\n')
    handles=watch_open(monkeypatch)
    module.CreateFiles('TestData',count)
    expected={f'TestData.{i:03d}' for i in range(1,count+1)}
    assert {p.name for p in Path('.').iterdir()}==expected
    assert all(Path(n).read_text()=='This is File '+n+'\n' for n in expected)
    assert handles and all(h.closed for h in handles)
