from pathlib import Path
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('parts',[[],['Hello Jack'],['first','ends with spaces  ','***x']])
def test_terminator_not_written_count_excludes_newlines(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,parts):
    """9618_w23_23:8(a) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('newfile.txt').write_text('obsolete contents\n')
    stream=iter(parts+['****'])
    calls=[]
    def data():
        calls.append(1)
        return next(stream)
    monkeypatch.setattr(module,'GetData',data)
    handles=watch_open(monkeypatch)
    module.ReceiveFile('newfile.txt')
    assert Path('newfile.txt').read_text()==''.join(p+'\n' for p in parts)
    assert output_lines(capsys.readouterr().out)==[f'{sum(map(len,parts))} characters were written to newfile.txt']
    assert len(calls)==len(parts)+1
    assert handles and all(h.closed for h in handles)
