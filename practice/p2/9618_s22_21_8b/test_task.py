import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('index',[0,26,499])
def test_found_including_last_row(sol,candidate_path,monkeypatch,capsys,index):
    """9618_s22_21:8(b) MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Secret[index]=['site.example','cipher']
    monkeypatch.setattr(sol,'Decrypt',lambda value:'FxAf-3haV-Tq49' if value=='cipher' else 'wrong')
    assert sol.FindPassword('site.example')=='FxAf-3haV-Tq49'
    assert capsys.readouterr().out==''

def test_absent_with_unused_holes(sol,capsys):
    """9618_s22_21:8(b) MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    sol.Secret[100]=['another.example','encrypted:x']
    assert sol.FindPassword('missing.example')==''
    assert capsys.readouterr().out.strip()
