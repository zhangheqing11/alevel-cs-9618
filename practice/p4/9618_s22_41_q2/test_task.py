import pytest
from testkit import feed_input, run_script

def test_2a_constructor_private_values(sol):
    """9618_s22_41:2(a) MP2, MP4-MP5: private attributes and initial values."""
    a = sol.Balloon("Shield", "Red")
    b = sol.Balloon("Umbrella", "Blue")
    for obj, item, colour in [(a, "Shield", "Red"), (b, "Umbrella", "Blue")]:
        assert vars(obj)["_Balloon__Health"] == 100
        assert vars(obj)["_Balloon__DefenceItem"] == item
        assert vars(obj)["_Balloon__Colour"] == colour

def test_2b_getter(sol):
    """9618_s22_41:2(b) MP2: returns the object's defence item."""
    assert sol.Balloon("Cape", "Blue").GetDefenceItem() == "Cape"

def test_2c_change_health_accumulates(sol):
    """9618_s22_41:2(c) MP2: adds positive and negative changes."""
    obj = sol.Balloon("Cape", "Blue")
    obj.ChangeHealth(-75)
    obj.ChangeHealth(10)
    assert vars(obj)["_Balloon__Health"] == 35

@pytest.mark.parametrize("change, dead", [(-99, False), (-100, True), (-101, True), (20, False)])
def test_2d_health_zero_boundary(sol, change, dead):
    """9618_s22_41:2(d) MP1-MP2: zero and negative health are True."""
    obj = sol.Balloon("Shield", "Red")
    obj.ChangeHealth(change)
    assert obj.CheckHealth() is dead

@pytest.mark.parametrize("strength", [50, 100, 130])
def test_2f_defend_calls_methods_and_returns_object(sol, monkeypatch, capsys, strength):
    """9618_s22_41:2(f) MP2-MP10: input, subtraction, getters, status, return."""
    class Target:
        def __init__(self): self.health, self.calls = 100, []
        def ChangeHealth(self, delta): self.health += delta; self.calls.append("change")
        def GetDefenceItem(self): self.calls.append("get"); return "Shield"
        def CheckHealth(self): self.calls.append("check"); return self.health <= 0
    target = Target()
    feed_input(monkeypatch, str(strength))
    assert sol.Defend(target) is target
    assert target.health == 100 - strength
    assert sorted(target.calls) == ["change", "check", "get"]
    lines = capsys.readouterr().out.splitlines()
    assert any("Shield" in line for line in lines)
    assert len(lines) >= 2  # appropriate message semantics checked manually

def test_2g_ii_screenshot_shield(candidate_path, exercise_dir):
    """9618_s22_41:2(e) MP1-MP3; 2(g)(i) MP1-MP2; 2(g)(ii) whole."""
    result = run_script(candidate_path, stdin="Shield\nRed\n50\n")
    assert result.returncode == 0, result.stderr
    assert "Shield" in result.stdout
    assert len(result.lines) >= 2


def test_2e_2gi_main_call_chain(candidate_path, exercise_dir):
    """9618_s22_41:2(e) MS p.23; 9618_s22_41:2(g)(i) MS p.26: 2(e) MP1–MP3; 2(g)(i) MP1; observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='Shield\nRed\n50\n', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    init = r.called("Balloon.__init__")
    assert any(list(c.args.values()) == ["Shield", "Red"] for c in init)
    defend = r.called("Defend")
    assert len(defend) == 1
    balloon = list(defend[0].args.values())[0]
    assert isinstance(balloon, type(defend[0].result)) and defend[0].result is balloon
    assert r.called("ChangeHealth") and list(r.called("ChangeHealth")[0].args.values()) == [-50]
    assert r.called("GetDefenceItem") and r.called("GetDefenceItem")[0].result in r.stdout
    assert r.called("CheckHealth") and r.called("CheckHealth")[0].result is False
