from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open,no_shortcuts

@pytest.mark.parametrize('data,target,expected',[('',1,True),('0001ABCDEPrinter cable long',1,False),('0001ABCDEPrinter cable long\n',5999,True),('0003ABCDEPrinter cable long\n0500FGHIJMouse mat large\n5999ABCDEUSB drive 32 GB',3,False),('0003ABCDEPrinter cable long\n0500FGHIJMouse mat large\n5999ABCDEUSB drive 32 GB',500,False),('0003ABCDEPrinter cable long\n0500FGHIJMouse mat large\n5999ABCDEUSB drive 32 GB',5999,False),('0003ABCDEPrinter cable long\n0500FGHIJMouse mat large\n5999ABCDEUSB drive 32 GB',1,True),('0003ABCDEPrinter cable long\n0500FGHIJMouse mat large\n5999ABCDEUSB drive 32 GB',400,True)])
def test_sorted_stock_lookup(candidate_path,exercise_dir,tmp_path,monkeypatch,data,target,expected):
    """9618_s23_21:8(b) MP1,2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('Stock.txt').write_text(data)
    handles=watch_open(monkeypatch)
    assert module.CheckNewItem(f'{target:04d}KLMNOAdditional product') is expected
    assert Path('Stock.txt').read_text()==data
    assert handles and all(h.closed for h in handles)
