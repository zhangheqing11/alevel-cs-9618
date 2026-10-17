from pathlib import Path
import pytest
from testkit import output_lines
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('size,count,newline',[(1,1,True),(204,3,False),(1,0,False),(8998,2,True)])
def test_append_new_ids_zero_points(candidate_path,exercise_dir,tmp_path,monkeypatch,capsys,size,count,newline):
    """9618_s25_21:7(b)(i) MP1,2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    old='\n'.join(f'{100000+i},{i%11}' for i in range(1,size+1))+('\n' if newline else '')
    Path('Loyalty.txt').write_text(old)
    handles=watch_open(monkeypatch)
    module.AddNewCustomers(count)
    newids=[str(100000+size+i) for i in range(1,count+1)]
    assert output_lines(capsys.readouterr().out)==newids
    expected=old+('\n' if count and not newline else '')+''.join(i+',0\n' for i in newids)
    assert Path('Loyalty.txt').read_text()==expected
    assert len(handles)>=2 and all(h.closed for h in handles)
