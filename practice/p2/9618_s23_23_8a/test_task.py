from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('lines,expected,count',[([],[],0),(['0001DRGPrinter cable long'],['0001XYZPrinter cable long'],1),(['0001ABCDescription DRG kept','0500DRGUSB cable 3 metre','5999DRGMouse mat 320 mm'],['0001ABCDescription DRG kept','0500XYZUSB cable 3 metre','5999XYZMouse mat 320 mm'],2)])
def test_only_supplier_field_changes(candidate_path,exercise_dir,tmp_path,monkeypatch,lines,expected,count):
    """9618_s23_23:8(a) MP1,2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    data='\n'.join(lines)
    Path('Stock.txt').write_text(data)
    Path('NewStock.txt').write_text('obsolete\n')
    handles=watch_open(monkeypatch)
    assert module.ChangeSupp('DRG','XYZ')==count
    assert Path('NewStock.txt').read_text()==''.join(line+'\n' for line in expected)
    assert Path('Stock.txt').read_text()==data
    assert len(handles)>=2 and all(h.closed for h in handles)
