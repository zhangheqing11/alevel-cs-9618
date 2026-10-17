from pathlib import Path
from practice.p2._test_support import load_at,watch_open

def test_all_record_fields_delimiters_and_overwrite(candidate_path,exercise_dir,tmp_path,monkeypatch):
    """9618_w24_22:8(b) MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    module.Character=[module.CharacterType(i%7,'Role '+str(i%3),'Name '+str(i),i*2) for i in range(45)]
    Path('SaveFile.txt').write_text('obsolete\n')
    handles=watch_open(monkeypatch)
    module.Save()
    assert Path('SaveFile.txt').read_text()==''.join(f'{i%7}^Role {i%3}^Name {i}^{i*2}\n' for i in range(45))
    assert handles and all(h.closed for h in handles)
