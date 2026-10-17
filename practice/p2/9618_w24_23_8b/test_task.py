from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('newline',[True,False])
def test_restore_full_save_and_conversions(candidate_path,exercise_dir,tmp_path,monkeypatch,newline):
    """9618_w24_23:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    records=[(i%7,'Role '+str(i%3),'Person '+str(i),i*2) for i in range(45)]
    Path('SaveFile.txt').write_text('\n'.join('|'.join(map(str,r)) for r in records)+('\n' if newline else ''))
    handles=watch_open(monkeypatch)
    module.Restore()
    assert [(c.Player,c.Role,c.Name,c.SkillLevel) for c in module.Character]==records
    assert all(type(c.Player) is int and type(c.SkillLevel) is int for c in module.Character)
    assert handles and all(h.closed for h in handles)

def test_uses_extract_for_each_field(candidate_path,exercise_dir,tmp_path,monkeypatch):
    """9618_w24_23:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('SaveFile.txt').write_text('\n'.join('record'+str(i) for i in range(45)))
    calls=[]
    def extract(line,field):
        calls.append((line,field))
        return ['3','Teacher','Name '+line,'65'][field-1]
    monkeypatch.setattr(module,'Extract',extract)
    module.Restore()
    assert sorted(calls)==sorted(('record'+str(i),f) for i in range(45) for f in range(1,5))
    assert module.Character[44].Name=='Name record44'
