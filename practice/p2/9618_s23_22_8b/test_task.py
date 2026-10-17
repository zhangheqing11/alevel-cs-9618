from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('ids,new,final_newline',[([],1,False),([500],1,False),([500],5999,True),([3,500,5998],1,True),([3,500,5998],400,False),([3,500,5998],5999,False)])
def test_insert_all_positions(candidate_path,exercise_dir,tmp_path,monkeypatch,ids,new,final_newline):
    """9618_s23_22:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    lines=[f'{n:04d}ABCProduct number {n:04d}' for n in ids]
    data='\n'.join(lines)+('\n' if final_newline else '')
    Path('Stock.txt').write_text(data)
    Path('NewStock.txt').write_text('old output must disappear')
    added=f'{new:04d}DEFNew product description'
    expected=[f'{n:04d}ABCProduct number {n:04d}' if n!=new else added for n in sorted(ids+[new])]
    handles=watch_open(monkeypatch)
    module.AddItem(added)
    assert Path('NewStock.txt').read_text()==''.join(line+'\n' for line in expected)
    assert Path('Stock.txt').read_text()==data
    assert len(handles)>=2 and all(h.closed for h in handles)
