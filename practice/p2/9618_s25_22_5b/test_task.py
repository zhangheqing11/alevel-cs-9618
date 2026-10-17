from pathlib import Path
import re
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,expected',[('081230',{8:1}),('000000\n000100\n152235\n235959\n',{0:2,15:1,23:1}),('081230\n081300\n150001\n152235\n180000',{8:2,15:2,18:1})])
def test_hour_counts_single_and_last_group(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,data,expected):
    """9618_s25_22:5(b) MP1,2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('TimeTaken.txt').write_text(data)
    handles=watch_open(monkeypatch)
    module.main()
    actual={}
    for line in output_lines(capsys.readouterr().out):
        match=re.fullmatch(r'Hour\s*:\s*(\d{1,2})\s+Total\s*:\s*(\d+)',line)
        assert match
        hour,total=map(int,match.groups())
        assert hour not in actual
        actual[hour]=total
    assert actual==expected
    assert handles and all(h.closed for h in handles)
