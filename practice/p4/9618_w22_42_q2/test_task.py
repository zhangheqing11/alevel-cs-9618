"""Tests use 9618_w22_42 MS, corpus point numbering."""
import runpy
import re
import pytest
from testkit import feed_input,run_script,use_files


def test_2a_private_initialisation(sol):
    """9618_w22_42:2(a) MP2-MP4: private attributes initialised from parameters."""
    c=sol.Character('Test',-2,93)
    assert (c._Character__Name,c._Character__XCoordinate,c._Character__YCoordinate)==('Test',-2,93)


def test_2b_getters(sol):
    """9618_w22_42:2(b) MP2-MP3: all three getters."""
    c=sol.Character('A',14,75)
    assert (c.GetName(),c.GetX(),c.GetY())==('A',14,75)


def test_2c_change_adds(sol):
    """9618_w22_42:2(c) MP2: add signed changes to existing coordinates."""
    c=sol.Character('A',14,75)
    c.ChangePosition(-3,6);c.ChangePosition(1,-2)
    assert (c.GetX(),c.GetY())==(12,79)


def test_2d_all_file_objects(candidate_path,monkeypatch,tmp_path,exercise_dir):
    """9618_w22_42:2(d) MP1-MP6: ten triples, integer conversion, objects in array."""
    work=use_files(monkeypatch,tmp_path,exercise_dir/'files')
    raw=(work/'Characters.txt').read_text().splitlines()
    feed_input(monkeypatch,'qui','A')
    ns=runpy.run_path(str(candidate_path),run_name='__main__')
    arrays=[v for v in ns.values() if isinstance(v,list) and len(v)==10 and all(isinstance(c,ns['Character']) for c in v)]
    assert arrays,'no ten-element Character array in main program'
    expected=[(raw[i],int(raw[i+1])-(1 if raw[i].lower()=='qui' else 0),int(raw[i+2])) for i in range(0,30,3)]
    assert [(c.GetName(),c.GetX(),c.GetY()) for c in arrays[0]]==expected


def test_2d_missing_file(candidate_path):
    """9618_w22_42:2(d) MP8-MP9: missing file is caught with output."""
    r=run_script(candidate_path)
    assert r.stdout.strip()
    assert 'FileNotFoundError' not in r.stderr


@pytest.mark.parametrize('move,x,y',[('A',83,9),('D',85,9),('W',84,10),('S',84,8)])
def test_2e_f_g_moves(candidate_path,exercise_dir,move,x,y):
    """9618_w22_42:2(e) MP1-MP6; 2(f) MP1-MP7; 2(g)(i) MP1-MP2."""
    r=run_script(candidate_path,stdin=f'THOMAS\nQUI\nX\n{move}\n',files_dir=exercise_dir/'files')
    assert r.returncode==0,r.stderr
    assert re.search(r'qui.*X\s*=\s*'+str(x)+r'.*Y\s*=\s*'+str(y),r.stdout,re.I)


def test_2gii_screenshot(candidate_path,exercise_dir):
    """9618_w22_42:2(g)(ii) whole: THOMAS, qui, X, A -> Qui, 83, 9 (MS p.20)."""
    r=run_script(candidate_path,stdin='THOMAS\nqui\nX\nA\n',files_dir=exercise_dir/'files')
    assert r.returncode==0,r.stderr
    assert re.search(r'qui.*83.*9',r.stdout,re.I)
