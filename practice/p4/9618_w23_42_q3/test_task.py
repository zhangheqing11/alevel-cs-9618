"""9618_w23_42 Q3 exact MS: fixed 2023 age and learning percentages."""
import datetime
import runpy
import re
import pytest
from testkit import run_script


def test_3ai_aii_constructor_and_getters(sol):
    """9618_w23_42:3(a)(i) MP4-MP5; 3(a)(ii) MP2-MP3."""
    dob=datetime.datetime(2005,12,31);c=sol.Character('Other',dob,62.5,7)
    assert c.GetName()=='Other' and c.GetIntelligence()==62.5
    assert any(k.endswith('Speed') and v==7 for k,v in vars(c).items())
    assert any(k.endswith('DateOfBirth') and v==dob for k,v in vars(c).items())


def test_3aiii_setter(sol):
    """9618_w23_42:3(a)(iii) MP2: assigns rather than adds."""
    c=sol.Character('A',datetime.datetime(2019,1,1),70,30)
    c.SetIntelligence(28.5);assert c.GetIntelligence()==28.5


def test_3aiv_learn(sol):
    """9618_w23_42:3(a)(iv) whole: ten percent increase, stored for next call."""
    c=sol.Character('A',datetime.datetime(2019,1,1),70,30)
    c.Learn();assert c.GetIntelligence()==pytest.approx(77)
    c.Learn();assert c.GetIntelligence()==pytest.approx(84.7)


@pytest.mark.parametrize('dob,age',[(datetime.datetime(2005,1,1),18),(datetime.datetime(2005,12,31),18),(datetime.datetime(2023,12,31),0)])
def test_3av_age_uses_2023_and_year_only(sol,dob,age):
    """9618_w23_42:3(a)(v) MP1-MP2: integer 2023 minus birth year; ignore month/day."""
    c=sol.Character('A',dob,70,30)
    assert c.ReturnAge()==age and isinstance(c.ReturnAge(),int)


@pytest.mark.parametrize('element,factor',[('fire',1.2),('water',1.2),('earth',1.3),('air',1.1)])
def test_3cii_magic_learning(sol,element,factor):
    """9618_w23_42:3(c)(ii) MP1-MP3: override and all element branches."""
    c=sol.MagicCharacter(element,'A',datetime.datetime(2018,3,3),75,22)
    c.Learn();assert c.GetIntelligence()==pytest.approx(75*factor)


def test_3ci_parent_constructor(sol,monkeypatch):
    """9618_w23_42:3(c)(i) MP1, MP3-MP5: inherit, parent initialisation, Element."""
    calls=[];original=sol.Character.__init__
    def spy(self,*args):calls.append(args);original(self,*args)
    monkeypatch.setattr(sol.Character,'__init__',spy)
    dob=datetime.datetime(2018,3,3)
    assert issubclass(sol.MagicCharacter,sol.Character)
    c=sol.MagicCharacter('earth','B',dob,31,2)
    assert calls==[('B',dob,31,2)]
    assert any(k.endswith('Element') and v=='earth' for k,v in vars(c).items())


def test_3bi_di_named_instances(candidate_path):
    """9618_w23_42:3(b)(i) MP1-MP2; 3(d)(i) MP1-MP2: correct objects."""
    ns=runpy.run_path(str(candidate_path),run_name='__main__')
    a=ns['FirstCharacter'];b=ns['FirstMagic']
    assert isinstance(a,ns['Character']) and isinstance(b,ns['MagicCharacter'])
    assert (a.GetName(),a.ReturnAge(),a.GetIntelligence())==('Royal',4,77)
    assert (b.GetName(),b.ReturnAge(),b.GetIntelligence())==('Light',5,90)


def test_3biii_royal_screenshot(candidate_path):
    """9618_w23_42:3(b)(ii) MP1-MP3; 3(b)(iii) whole: Royal, 4, 77."""
    r=run_script(candidate_path);assert r.returncode==0,r.stderr
    assert re.search(r'Royal\D+4\D+77(?:\.0)?\b',r.stdout)


def test_3diii_magic_screenshot(candidate_path):
    """9618_w23_42:3(d)(ii) whole; 3(d)(iii) whole: Light, 5, 90 from MS p.34."""
    r=run_script(candidate_path);assert r.returncode==0,r.stderr
    assert re.search(r'Light\D+5\D+90(?:\.0)?\b',r.stdout)
