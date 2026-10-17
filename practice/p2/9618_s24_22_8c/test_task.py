from pathlib import Path
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,expected,count',[('',[],0),('   //only comment',[],1),('  OUTPUT 1',['OUTPUT 1'],0),('  DECLARE X : INTEGER\n\n    \n  //comment\n  X <- 2//tail',['DECLARE X : INTEGER','X <- 2'],3)])
def test_append_clean_lines(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,data,expected,count):
    """9618_s24_22:8(c) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('input.txt').write_text(data)
    Path('output.txt').write_text('existing line\n')
    handles=watch_open(monkeypatch)
    module.Stage_2('input.txt','output.txt')
    assert Path('output.txt').read_text()=='existing line\n'+''.join(s+'\n' for s in expected)
    assert output_lines(capsys.readouterr().out)==[str(count)+' blank lines were removed']
    assert Path('input.txt').read_text()==data
    assert len(handles)>=2 and all(h.closed for h in handles)

def test_uses_both_provided_modules(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys):
    """9618_s24_22:8(c) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('input.txt').write_text('  token')
    Path('output.txt').write_text('')
    calls=[]
    def spaces(line):
        calls.append(('spaces',line))
        return line.lstrip(' ')
    def comment(line):
        calls.append(('comment',line))
        return ''
    monkeypatch.setattr(module,'DeleteSpaces',spaces)
    monkeypatch.setattr(module,'DeleteComment',comment)
    module.Stage_2('input.txt','output.txt')
    assert len(calls)==2 and {c[0] for c in calls}=={'spaces','comment'}
    assert Path('output.txt').read_text()==''
