from pathlib import Path
import re
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,expected',[('',[]),('1234DRGUSB Printer Cable 3m',[('1234','USB Printer Cable 3m')]),('1234DRGUSB Printer Cable 3m\n1273DRG32GB USB Flash Drive\n1300ABCDRG in description kept\n1350DRGMouse Mat 320 x 240 mm\n',[('1234','USB Printer Cable 3m'),('1273','32GB USB Flash Drive'),('1350','Mouse Mat 320 x 240 mm')])])
def test_report_fields_and_count(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,data,expected):
    """9618_s23_23:8(b) MP2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('Stock.txt').write_text(data)
    handles=watch_open(monkeypatch)
    module.Report_1('DRG')
    lines=output_lines(capsys.readouterr().out)
    assert lines[0]=='Report for Supplier: DRG'
    assert lines[1].split()==['Item','Description']
    assert lines[-1]=='Number of items listed: '+str(len(expected))
    records=[]
    for line in lines[2:-1]:
        match=re.fullmatch(r'(\d{4})\s+(.+)',line)
        assert match is not None
        records.append(match.groups())
    assert records==expected
    assert Path('Stock.txt').read_text()==data
    assert handles and all(h.closed for h in handles)
