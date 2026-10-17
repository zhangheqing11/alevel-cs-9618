from pathlib import Path
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('marks',[[],[41],[40],[65,57,46,41,0,75,29]])
def test_exact_candidate_count_and_new_file(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,marks):
    """9618_w24_21:8(b) MP2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    module.Result=[[m,1000000+i] for i,m in enumerate(marks)]+[[43,9999999]]
    Path('GRList.txt').write_text('old\n')
    calls=[]
    def check(mark):
        calls.append(mark)
        return any(abs(mark-g)<=2 for g in module.GradeBoundary)
    monkeypatch.setattr(module,'CheckMark',check)
    handles=watch_open(monkeypatch)
    module.CheckAll(len(marks))
    expected=[str(1000000+i) for i,m in enumerate(marks) if any(abs(m-g)<=2 for g in module.GradeBoundary)]
    assert Path('GRList.txt').read_text()==''.join(i+'\n' for i in expected)
    assert output_lines(capsys.readouterr().out)==[f'There are {len(expected)} papers to check']
    assert calls==marks
    assert handles and all(h.closed for h in handles)
