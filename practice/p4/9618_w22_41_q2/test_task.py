"""Exact matching 9618_w22_41 MS, Question 2; corpus MP numbers."""
import runpy
from testkit import run_script


def test_2ai_card_private_constructor(sol):
    """9618_w22_41:2(a)(i) MP1-MP5; comments/header reviewed manually."""
    for n,c in [(1,'red'),(5,'blue'),(3,'yellow')]:
        obj=sol.Card(n,c)
        assert obj._Card__Number == n and obj._Card__Colour == c


def test_2aii_getters(sol):
    """9618_w22_41:2(a)(ii) MP2-MP3: both getters return their attributes."""
    obj=sol.Card(4,'yellow')
    assert obj.GetNumber()==4 and obj.GetColour()=='yellow'


def test_2bi_hand_constructor(sol):
    """9618_w22_41:2(b)(i) MP1-MP6: ten slots, five objects, pointer/count."""
    cards=[sol.Card(n,'blue') for n in range(1,6)]
    h=sol.Hand(*cards)
    assert len(h._Hand__Cards)==10
    assert all(h._Hand__Cards[i] is cards[i] for i in range(5))
    assert h._Hand__FirstCard==0 and h._Hand__NumberCards==5


def test_2bii_getcard(sol):
    """9618_w22_41:2(b)(ii) MP2: return the object at the supplied index."""
    cards=[sol.Card(n,'red') for n in range(1,6)]
    h=sol.Hand(*cards)
    assert all(h.GetCard(i) is cards[i] for i in range(5))


def test_2ci_score_all_five(sol):
    """9618_w22_41:2(c)(i) MP1-MP6: colour points, numbers, all five, return."""
    for colour,bonus in [('red',5),('blue',10),('yellow',15)]:
        h=sol.Hand(*(sol.Card(n,colour) for n in range(1,6)))
        assert sol.CalculateValue(h)==15+5*bonus


def test_2ci_getter_protocol(sol):
    """9618_w22_41:2(c)(i) MP2-MP5: use GetCard/GetNumber/GetColour."""
    visits=[]
    class Card:
        def GetNumber(self): return 2
        def GetColour(self): return 'blue'
    class Hand:
        def GetCard(self,i): visits.append(i); return Card()
    assert sol.CalculateValue(Hand())==60
    assert sorted(visits)==list(range(5))


def test_2aiii_biii_main_objects(candidate_path):
    """9618_w22_41:2(a)(iii) MP1-MP2; 9618_w22_41:2(b)(iii) MP1-MP2."""
    ns=runpy.run_path(str(candidate_path),run_name='__main__')
    values=[]
    for value in ns.values():
        values.extend(value if isinstance(value,list) else [value])
    cards=[v for v in values if isinstance(v,ns['Card'])]
    assert {(c.GetNumber(),c.GetColour()) for c in cards}=={(n,c) for n in range(1,6) for c in ['red','blue','yellow']}
    hands=[v for v in ns.values() if isinstance(v,ns['Hand'])]
    values=[[(h.GetCard(i).GetNumber(),h.GetCard(i).GetColour()) for i in range(5)] for h in hands]
    assert [(1,'red'),(2,'red'),(3,'red'),(4,'red'),(1,'yellow')] in values
    assert [(2,'yellow'),(3,'yellow'),(4,'yellow'),(5,'yellow'),(1,'blue')] in values


def test_2ciii_screenshot_player2(candidate_path):
    """9618_w22_41:2(c)(iii) whole; 9618_w22_41:2(c)(ii) MP1-MP3: player 2 wins."""
    res=run_script(candidate_path)
    assert res.returncode==0,res.stderr
    assert any('2' in line for line in res.lines)


def test_2cii_main_call_chain(candidate_path, exercise_dir):
    """9618_w22_41:2(c)(ii) MS p.15: 2(c)(ii) MP1–MP2; observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    scores = r.called("CalculateValue")
    assert len(scores) == 2 and [c.result for c in scores] == [46,85]
    hands = [list(c.args.values())[0] for c in scores]
    assert [[(h.GetCard(i).GetNumber(),h.GetCard(i).GetColour()) for i in range(5)] for h in hands] == [
        [(1,"red"),(2,"red"),(3,"red"),(4,"red"),(1,"yellow")],
        [(2,"yellow"),(3,"yellow"),(4,"yellow"),(5,"yellow"),(1,"blue")]]
    assert "2" in r.stdout
