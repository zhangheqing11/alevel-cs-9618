import re
from testkit import run_script

def nums(text): return [int(x) for x in re.findall(r"-?\d+", text)]

def test_2a_i_constructor_private(sol):
    """9618_s23_41:2(a)(i) MP2, MP4-MP5: all five private attributes."""
    v = sol.Vehicle("Test", 35, 12)
    assert vars(v) == {"_Vehicle__ID":"Test", "_Vehicle__MaxSpeed":35, "_Vehicle__IncreaseAmount":12, "_Vehicle__CurrentSpeed":0, "_Vehicle__HorizontalPosition":0}

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
    assert nums(capsys.readouterr().out) == [20,20]
    h=sol.Helicopter("H",200,30,7,20); h.IncreaseSpeed(); h.OutputCurrentPosition()
    assert nums(capsys.readouterr().out) == [30,30,7]

def test_2d_ii_screenshot(candidate_path):
    """9618_s23_41:2(d)(i) MP1-MP5; 2(d)(ii) whole: official 60,40 / 120,80,6."""
    result=run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert nums(result.stdout) == [60,40,120,80,6]
