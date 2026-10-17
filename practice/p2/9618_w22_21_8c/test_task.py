from pathlib import Path
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('valid,codes,limit,expected,read_count',[(False,[1],2,'That program file is not valid',0),(True,[0,3,0,4]+[0]*6,2,'There were 2 errors.',10),(True,[1,0,2,3]+[4]*6,2,'Check terminated - too many errors',4),(True,[0]*9+[5],0,'Check terminated - too many errors',10),(True,[0]*10,0,'There were 0 errors.',10)])
def test_validity_threshold_and_final_line(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,valid,codes,limit,expected,read_count):
    """9618_w22_21:8(c) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('project.txt').write_text('\n'.join(str(i) for i in range(len(codes))))
    checks=[]
    monkeypatch.setattr(module,'CheckFile',lambda name:valid)
    def check(line):
        checks.append(line)
        return codes[int(line)]
    monkeypatch.setattr(module,'CheckLine',check)
    handles=watch_open(monkeypatch)
    module.CountErrors('project.txt',limit)
    assert output_lines(capsys.readouterr().out)==[expected]
    assert len(checks)==read_count
    assert all(h.closed for h in handles)
