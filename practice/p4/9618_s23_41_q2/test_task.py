import re
from testkit import run_script

def nums(text): return [int(x) for x in re.findall(r"-?\d+", text)]

def test_2a_i_constructor_private(sol):
    """9618_s23_41:2(a)(i) MP2, MP4-MP5: all five private attributes."""
    v = sol.Vehicle("Test", 35, 12)
    expected = {"_Vehicle__ID":"Test", "_Vehicle__MaxSpeed":35, "_Vehicle__IncreaseAmount":12, "_Vehicle__CurrentSpeed":0, "_Vehicle__HorizontalPosition":0}
    assert all(vars(v).get(k) == value for k,value in expected.items())

def test_2a_ii_iii_getters_setters(sol):
    """9618_s23_41:2(a)(ii) MP2-MP3; 2(a)(iii) MP2-MP3: reads/writes correct fields."""
    v = sol.Vehicle("Test", 35, 12)
    v.SetCurrentSpeed(9)
    v.SetHorizontalPosition(27)
    assert (v.GetCurrentSpeed(), v.GetHorizontalPosition(), v.GetMaxSpeed(), v.GetIncreaseAmount()) == (9,27,35,12)

def test_2a_iv_speed_clamps_position_still_changes(sol):
    """9618_s23_41:2(a)(iv) MP1-MP3: positive increase, cap, add updated speed in every case."""
    v = sol.Vehicle("Test", 35, 12)
    for speed,pos in [(12,12),(24,36),(35,71),(35,106)]:
        v.IncreaseSpeed()
        assert (v.GetCurrentSpeed(), v.GetHorizontalPosition()) == (speed,pos)

def test_2b_i_inheritance_private_fields(sol):
    """9618_s23_41:2(b)(i) MP1-MP2, MP4-MP5: inheritance and parent/child initial state."""
    assert issubclass(sol.Helicopter, sol.Vehicle)
    h = sol.Helicopter("H",35,12,7,15)
    assert h.GetMaxSpeed() == 35 and h.GetIncreaseAmount() == 12
    assert vars(h)["_Helicopter__VerticalPosition"] == 0
    assert vars(h)["_Helicopter__VerticalChange"] == 7
    assert vars(h)["_Helicopter__MaxHeight"] == 15

def test_2b_ii_height_and_speed_caps(sol):
    """9618_s23_41:2(b)(ii) MP2-MP4: child height cap and inherited horizontal behavior."""
    h = sol.Helicopter("H",35,12,7,15)
    for speed,pos,height in [(12,12,7),(24,36,14),(35,71,15),(35,106,15)]:
        h.IncreaseSpeed()
        assert (h.GetCurrentSpeed(),h.GetHorizontalPosition(),vars(h)["_Helicopter__VerticalPosition"]) == (speed,pos,height)

def test_2c_outputs_vehicle_and_helicopter(sol, capsys):
    """9618_s23_41:2(c) MP1-MP3: horizontal/speed for both; height only for helicopter."""
    v=sol.Vehicle("V",100,20); v.IncreaseSpeed(); v.OutputCurrentPosition()
    assert contains_values(capsys.readouterr().out, [20,20])
    h=sol.Helicopter("H",200,30,7,20); h.IncreaseSpeed(); h.OutputCurrentPosition()
    assert contains_values(capsys.readouterr().out, [30,30,7])

def test_2d_ii_screenshot(candidate_path):
    """9618_s23_41:2(d)(i) MP1-MP5; 2(d)(ii) whole: official 60,40 / 120,80,6."""
    result=run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert contains_values(result.stdout, [60,40,120,80,6])


def contains_values(text, expected):
    """D31/D46: compare required values in order, allowing explanatory text."""
    values = iter(float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text))
    return all(any(abs(value - wanted) < 1e-7 for value in values) for wanted in expected)


def test_2main_call_chain(candidate_path, exercise_dir):
    """9618_s23_41:2(d)(i) MS p.24; 9618_s23_41:2(b)(i) MS p.18: observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    v = r.called("Vehicle.__init__")
    assert [list(c.args.values()) for c in v] == [["Tiger",100,20],["Lion",350,40]]
    assert [list(c.args.values()) for c in r.called("Helicopter.__init__")] == [["Lion",350,40,3,100]]
    assert len(r.called("Helicopter.IncreaseSpeed")) == 2
    # Parent calls from Helicopter are allowed; car still needs its own two calls.
    assert len(r.called("Vehicle.IncreaseSpeed")) >= 2
    assert len(r.called("OutputCurrentPosition")) >= 2
