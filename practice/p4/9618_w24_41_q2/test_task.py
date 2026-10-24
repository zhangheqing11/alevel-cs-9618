"""9618_w24_41 Q2 exact MS: horse/fence objects and chance calculations."""
import re
import runpy
import pytest
from testkit import feed_input,run_script

DATA='152\n5\n121\n1\n130\n3\n145\n4\n'


def numbers(text): return [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',text)]


def has_values(text,expected):
    values=iter(numbers(text))
    return all(any(v==pytest.approx(w) for v in values) for w in expected)


def test_2ai_aii_horse(sol):
    """9618_w24_41:2(a)(i) MP2-MP4; 9618_w24_41:2(a)(ii) MP2-MP3."""
    h=sol.Horse('Fox',132,70)
    assert (h._Horse__Name,h._Horse__MaxFenceHeight,h._Horse__PercentageSuccess)==('Fox',132,70)
    assert h.GetName()=='Fox' and h.GetMaxFenceHeight()==132


def test_2ci_fence(sol):
    """9618_w24_41:2(c)(i) MP2-MP4: private attributes, constructor, two getters."""
    f=sol.Fence(145,4)
    assert (f._Fence__Height,f._Fence__Risk)==(145,4)
    assert (f.GetHeight(),f.GetRisk())==(145,4)


@pytest.mark.parametrize('height',[149,150,151])
@pytest.mark.parametrize('risk,modifier',[(1,1),(2,.9),(3,.8),(4,.7),(5,.6)])
def test_2d_success(sol,height,risk,modifier):
    """9618_w24_41:2(d) MP1-MP5: exact height boundary, all risk modifiers, return."""
    h=sol.Horse('Beauty',150,72)
    assert h.Success(height,risk)==pytest.approx(72*(.2 if height>150 else modifier))


def test_2bi_cii_main_arrays(candidate_path,monkeypatch):
    """9618_w24_41:2(b)(i) MP1-MP3; 9618_w24_41:2(c)(ii) MP1-MP3: arrays and object data."""
    feed_input(monkeypatch,*DATA.splitlines());ns=runpy.run_path(str(candidate_path),run_name='__main__')
    assert len(ns['Horses'])==2
    assert [(h.GetName(),h.GetMaxFenceHeight()) for h in ns['Horses']]==[('Beauty',150),('Jet',160)]
    assert [(f.GetHeight(),f.GetRisk()) for f in ns['Course']]==[(152,5),(121,1),(130,3),(145,4)]


def test_2bii_screenshot_names(candidate_path):
    """9618_w24_41:2(b)(i) MP4-MP5; 9618_w24_41:2(b)(ii) whole: both names."""
    r=run_script(candidate_path,stdin=DATA);assert r.returncode==0,r.stderr
    assert 'Beauty' in r.stdout and 'Jet' in r.stdout


def test_2cii_validation_boundaries(candidate_path,monkeypatch):
    """9618_w24_41:2(c)(ii) MP1-MP5: repeat invalid height/risk, accept endpoints."""
    feed_input(monkeypatch,'69','181','70','0','6','1','180','5','150','2','160','3')
    ns=runpy.run_path(str(candidate_path),run_name='__main__')
    assert [(f.GetHeight(),f.GetRisk()) for f in ns['Course']]==[(70,1),(180,5),(150,2),(160,3)]


def test_2eiii_screenshot_all_chances(candidate_path):
    """9618_w24_41:2(e)(i) MP1-MP3; 9618_w24_41:2(e)(ii) MP1-MP2; 9618_w24_41:2(e)(iii) MP1-MP2."""
    r=run_script(candidate_path,stdin=DATA);assert r.returncode==0,r.stderr
    assert has_values(r.stdout,[14.4,72,57.6,50.4,48.6,39,65,52,45.5,50.375])
    assert any('Jet' in line and ('highest' in line.lower() or 'win' in line.lower()) for line in r.lines)


def test_2eii_first_horse_can_win(candidate_path):
    """9618_w24_41:2(e)(ii) MP1-MP2: initial winner is first horse, not index -1."""
    r=run_script(candidate_path,stdin='70\n1\n70\n1\n70\n1\n70\n1\n')
    assert r.returncode==0,r.stderr
    assert has_values(r.stdout,[72,65])
    assert any('Beauty' in line and ('highest' in line.lower() or 'win' in line.lower()) for line in r.lines)


def test_2main_call_chain(candidate_path, exercise_dir):
    """9618_w24_41:2(b)(i) MS p.14; 9618_w24_41:2(e)(i) MS p.21; 9618_w24_41:2(e)(ii) MS p.22: observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='152\n5\n121\n1\n130\n3\n145\n4\n', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    calls = r.called("Success")
    args = [list(c.args.values()) for c in calls]
    from collections import Counter
    assert Counter(tuple(a) for a in args) == Counter({(152,5):2,(121,1):2,(130,3):2,(145,4):2})
    assert len(r.called("GetHeight")) >= 8 and len(r.called("GetRisk")) >= 8
    assert {c.result for c in r.called("GetName")} >= {"Beauty","Jet"}
    assert all(any(float(v) == pytest.approx(c.result) for v in re.findall(r"-?\d+(?:\.\d+)?",r.stdout)) for c in calls)
