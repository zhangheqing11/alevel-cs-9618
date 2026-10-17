from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,expected',[('one\ntwo\nthree',['one','two','three']),('first\nsecond\nthird\nfourth\nfifth\n',['third','fourth','fifth']),('A\n\nC\nD',['','C','D'])])
def test_last_three_lines(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,data,expected):
    """9618_s22_22:4(a) MP3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('sample.txt').write_text(data)
    handles=watch_open(monkeypatch)
    module.LastLines('sample.txt')
    assert capsys.readouterr().out.splitlines()==expected
    assert handles and all(handle.closed for handle in handles)
