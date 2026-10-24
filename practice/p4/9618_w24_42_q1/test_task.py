"""9618_w24_42 Q1 exact MS: event objects, score lookup and group winner."""
import runpy
import re
import pytest
from testkit import run_script


def test_1ai_aii_event(sol):
    """9618_w24_42:1(a)(i) MP2-MP4; 9618_w24_42:1(a)(ii) MP2-MP3: constructor/getters."""
    e=sol.EventItem('New','swim',4)
    assert (e.GetName(),e.GetEventType(),e.GetDifficulty())==('New','swim',4)
    assert e._EventItem__EventName=='New' and e._EventItem__Difficulty==4
    assert any(k.startswith('_EventItem__') and v=='swim' for k,v in vars(e).items())


def test_1c_character(sol):
    """9618_w24_42:1(c) MP2-MP4: private fields, parameters and name getter."""
    c=sol.Character('New',1,2,3,4)
    assert c.GetName()=='New'
    assert (c._Character__Jump,c._Character__Swim,c._Character__Run,c._Character__Drive)==(1,2,3,4)
    assert any(k.startswith('_Character__') and v=='New' for k,v in vars(c).items())


@pytest.mark.parametrize('skill',range(1,6))
@pytest.mark.parametrize('difficulty',range(1,6))
def test_1d_all_skills_difficulties(sol,skill,difficulty):
    """9618_w24_42:1(d) MP2-MP5: all types, >= boundary and differences 1..4."""
    for event_type in ['jump','swim','run','drive']:
        skills=[1,1,1,1];skills[['jump','swim','run','drive'].index(event_type)]=skill
        c=sol.Character('Test',*skills)
        expected=100 if skill>=difficulty else 100-20*(difficulty-skill)
        assert c.CalculateScore(event_type,difficulty)==expected


def test_1bi_bii_ei_main_objects(candidate_path):
    """9618_w24_42:1(b)(i) whole; 9618_w24_42:1(b)(ii) MP1-MP3; 9618_w24_42:1(e)(i) MP1-MP2."""
    ns=runpy.run_path(str(candidate_path),run_name='__main__')
    assert len(ns['Group'])>=5
    assert [(e.GetName(),e.GetEventType(),e.GetDifficulty()) for e in ns['Group'][:5]]==[
        ('Bridge','jump',3),('Water wade','swim',4),('100 mile run','run',5),('Gridlock','drive',2),('Wall on wall','jump',4)]
    cs={v.GetName():v for v in ns.values() if isinstance(v,ns['Character'])}
    assert [cs['Tarz'].CalculateScore(t,5) for t in ['jump','swim','run','drive']]==[100,60,100,20]
    assert [cs['Geni'].CalculateScore(t,5) for t in ['jump','swim','run','drive']]==[40,40,60,80]


def test_1eiii_screenshot(candidate_path):
    """9618_w24_42:1(e)(ii) MP1-MP4,MP6-MP7; 9618_w24_42:1(e)(iii) whole: winners and 4 points."""
    r=run_script(candidate_path);assert r.returncode==0,r.stderr
    winners=[re.search(r'\b(Tarz|Geni)\b',line).group(0) for line in r.lines if re.search(r'\b(Tarz|Geni)\b',line)]
    assert winners[:6]==['Tarz','Tarz','Tarz','Geni','Tarz','Tarz']
    assert re.search(r'Tarz[\s\S]*?\b4\b', r.stdout)


def test_1eii_main_call_chain(candidate_path, exercise_dir):
    """9618_w24_42:1(e)(ii) MS p.13: 1(e)(ii) MP2,MP7; observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    scores = r.called("CalculateScore")
    from collections import Counter
    assert Counter(tuple(c.args.values()) for c in scores) == Counter({("jump",3):2,("swim",4):2,("run",5):2,("drive",2):2,("jump",4):2})
    assert len(r.called("GetEventType")) >= 5 and len(r.called("GetDifficulty")) >= 5
    assert {c.result for c in r.called("GetName")} >= {"Tarz","Geni"}
