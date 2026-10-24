"""9618_w23_41 Q3: boundaries and polymorphic movement, exact matching MS."""
import re
import runpy
import pytest
from testkit import feed_input,run_script


def test_3ai_aii_construct_getters(sol):
    """9618_w23_41:3(a)(i) MP3-MP4; 9618_w23_41:3(a)(ii) MP2-MP3."""
    c=sol.Character(67,23,'A')
    assert (c.GetXPosition(),c.GetYPosition())==(67,23)
    assert any(k.endswith('Name') and v=='A' for k,v in vars(c).items())


@pytest.mark.parametrize('axis',['X','Y'])
def test_3aiii_clamps_and_accumulates(sol,axis):
    """9618_w23_41:3(a)(iii) MP2-MP4: add, clamp below 0 and above 10000, inclusive."""
    c=sol.Character(50,50,'A');setpos=getattr(c,'Set'+axis+'Position');getpos=getattr(c,'Get'+axis+'Position')
    for delta,expected in [(12,62),(-62,0),(-1,0),(10000,10000),(1,10000),(-1,9999)]:
        setpos(delta);assert getpos()==expected


@pytest.mark.parametrize('cls,step',[('Character',10),('BikeCharacter',20)])
@pytest.mark.parametrize('direction,dx,dy',[('up',0,1),('down',0,-1),('left',-1,0),('right',1,0)])
def test_3aiv_cii_move(sol,cls,step,direction,dx,dy):
    """9618_w23_41:3(a)(iv) MP2-MP4; 9618_w23_41:3(c)(ii) MP1-MP2: overriding Move."""
    c=getattr(sol,cls)(50,50,'A');c.Move(direction)
    assert (c.GetXPosition(),c.GetYPosition())==(50+step*dx,50+step*dy)


def test_3ci_inherits_parent(sol,monkeypatch):
    """9618_w23_41:3(c)(i) MP1-MP3: inherit, initialise via parent constructor."""
    calls=[];original=sol.Character.__init__
    def spy(self,*args):calls.append(args);original(self,*args)
    monkeypatch.setattr(sol.Character,'__init__',spy)
    assert issubclass(sol.BikeCharacter,sol.Character)
    c=sol.BikeCharacter(78,24,'B')
    assert calls==[(78,24,'B')]
    assert (c.GetXPosition(),c.GetYPosition())==(78,24)


def test_3b_d_main_instances(candidate_path,monkeypatch):
    """9618_w23_41:3(b) MP1-MP2; 9618_w23_41:3(d) whole: Jack and Karla correct instances."""
    feed_input(monkeypatch,'jack','right');ns=runpy.run_path(str(candidate_path),run_name='__main__')
    assert isinstance(ns['Jack'],ns['Character']) and isinstance(ns['Karla'],ns['BikeCharacter'])
    assert (ns['Jack'].GetXPosition(),ns['Jack'].GetYPosition())==(60,50)
    assert (ns['Karla'].GetXPosition(),ns['Karla'].GetYPosition())==(100,50)


@pytest.mark.parametrize('name,direction,x,y',[('jack','right',60,50),('karla','down',100,30)])
def test_3eii_screenshots(candidate_path,name,direction,x,y):
    """9618_w23_41:3(e)(i) MP1-MP5; 9618_w23_41:3(e)(ii) MP1: exact two MS screenshot results."""
    r=run_script(candidate_path,stdin=f'{name}\n{direction}\n')
    assert r.returncode==0,r.stderr
    assert re.search(r'X\s*=\s*'+str(x)+r'.*Y\s*=\s*'+str(y),r.stdout, re.S)


def test_3ei_rejects_invalid_inputs(candidate_path):
    """9618_w23_41:3(e)(i) MP1-MP5: reject both invalid names and invalid directions."""
    r=run_script(candidate_path,stdin='nobody\njack\nforward\nright\n')
    assert r.returncode==0,r.stderr
    assert re.search(r'X\s*=\s*60.*Y\s*=\s*50',r.stdout, re.S)


def test_3main_call_chain(candidate_path, exercise_dir):
    """9618_w23_41:3(e)(i) MS p.35: observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='jack\nright\n', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    moves = r.called("Move")
    assert moves and all(list(c.args.values()) == ["right"] for c in moves)
    assert r.called("GetXPosition") and r.called("GetYPosition")
    assert str(r.called("GetXPosition")[-1].result) in r.stdout
    assert str(r.called("GetYPosition")[-1].result) in r.stdout
