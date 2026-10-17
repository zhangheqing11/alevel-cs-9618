from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,expected',[('',[]),('//comment',[]),('OUTPUT 1',['OUTPUT 1']),('DECLARE X : INTEGER\n\n//comment\n  X <- 2//tail\nOUTPUT X',['DECLARE X : INTEGER','  X <- 2','OUTPUT X'])])
def test_remove_comments_skip_empty_and_close(candidate_path,exercise_dir,tmp_path,monkeypatch,data,expected):
    """9618_s24_21:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('Ada_src.txt').write_text(data)
    Path('Ada_S1.txt').write_text('obsolete\n')
    handles=watch_open(monkeypatch)
    assert module.Stage_1('Ada')==len(expected)
    assert Path('Ada_S1.txt').read_text()==''.join(s+'\n' for s in expected)
    assert Path('Ada_src.txt').read_text()==data
    assert len(handles)>=2 and all(h.closed for h in handles)

def test_uses_provided_delete_comment(candidate_path,exercise_dir,tmp_path,monkeypatch):
    """9618_s24_21:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('Ada_src.txt').write_text('first\nsecond')
    calls=[]
    def delete(line):
        calls.append(line)
        return 'processed' if line=='first' else ''
    monkeypatch.setattr(module,'DeleteComment',delete)
    assert module.Stage_1('Ada')==1
    assert calls==['first','second']
    assert Path('Ada_S1.txt').read_text()=='processed\n'
