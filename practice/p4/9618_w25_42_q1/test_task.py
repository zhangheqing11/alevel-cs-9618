"""9618_w25_42 Q1 exact MS: movement and four screenshot cases."""
import re
import runpy
import pytest
from testkit import feed_input,run_script


def position(text):
    assert isinstance(text,str)
    m=re.fullmatch(r'X = (-?\d+(?:\.\d+)?) Y = (-?\d+(?:\.\d+)?)',text.strip())
    assert m,'GetPosition must return the QP string format'
    return tuple(map(float,m.groups()))


def test_1ai_aii_constructor_species(sol):
    """9618_w25_42:1(a)(i) MP2-MP4; 1(a)(ii) MP2: private data and 500 initial positions."""
    b=sol.Bird(63.5,'Pigeon')
    assert (b._Bird__Species,b._Bird__DistancePerHour,b._Bird__XPosition,b._Bird__YPosition)==('Pigeon',63.5,500,500)
    assert b.GetSpecies()=='Pigeon'


def test_1aiii_position_return(sol):
    """9618_w25_42:1(a)(iii) MP1-MP3: formatted string returned, not printed."""
    assert position(sol.Bird(56,'Macaw').GetPosition())==(500,500)


@pytest.mark.parametrize('direction,dx,dy',[('N',0,1),('S',0,-1),('E',1,0),('W',-1,0)])
@pytest.mark.parametrize('speed,minutes',[(71,60),(56,30),(0,500),(100,0),(100,500)])
def test_1aiv_moves(sol,direction,dx,dy,speed,minutes):
    """9618_w25_42:1(a)(iv) MP2-MP5: minutes/60, all directions, zero/endpoints."""
    b=sol.Bird(speed,'Test');b.Move(direction,minutes)
    distance=speed/60*minutes
    assert position(b.GetPosition())==pytest.approx((500+dx*distance,500+dy*distance))


def test_1b_main_objects(candidate_path,monkeypatch):
    """9618_w25_42:1(b) MP1-MP3: correct speeds/species stored in objects."""
    feed_input(monkeypatch,'1','60','N');ns=runpy.run_path(str(candidate_path),run_name='__main__')
    values=[]
    for v in ns.values():values.extend(v if isinstance(v,list) else [v])
    birds=[v for v in values if isinstance(v,ns['Bird'])]
    assert {(b.GetSpecies(),b._Bird__DistancePerHour) for b in birds}=={('Cockatiel',71),('Macaw',56)}


@pytest.mark.parametrize('choice,minutes,direction,name,x,y',[
    ('1',60,'N','Cockatiel',500,571),('2',30,'S','Macaw',500,472),
    ('1',30,'W','Cockatiel',464.5,500),('2',60,'E','Macaw',556,500)])
def test_1cii_four_screenshots(candidate_path,choice,minutes,direction,name,x,y):
    """9618_w25_42:1(c)(i) MP1-MP2,MP5-MP8; 1(c)(ii) MP1-MP3: four MS results."""
    r=run_script(candidate_path,stdin=f'{choice}\n{minutes}\n{direction}\n');assert r.returncode==0,r.stderr
    assert re.search(r'Cockatiel.*X\s*=\s*500(?:\.0)?.*Y\s*=\s*500',r.stdout)
    assert re.search(r'Macaw.*X\s*=\s*500(?:\.0)?.*Y\s*=\s*500',r.stdout)
    matches=re.findall(re.escape(name)+r'[^\n]*X\s*=\s*(-?\d+(?:\.\d+)?)\s+Y\s*=\s*(-?\d+(?:\.\d+)?)',r.stdout)
    assert tuple(map(float,matches[-1]))==pytest.approx((x,y))


@pytest.mark.parametrize('minutes',[0,500])
def test_1ci_validation(candidate_path,minutes):
    """9618_w25_42:1(c)(i) MP2-MP7: repeat invalid choice/time/direction, inclusive limits."""
    r=run_script(candidate_path,stdin=f'3\n0\n1\n-1\n501\n{minutes}\nQ\nN\n');assert r.returncode==0,r.stderr
    matches=re.findall(r'Cockatiel[^\n]*X\s*=\s*(-?\d+(?:\.\d+)?)\s+Y\s*=\s*(-?\d+(?:\.\d+)?)',r.stdout)
    assert tuple(map(float,matches[-1]))==pytest.approx((500,500+71/60*minutes))
