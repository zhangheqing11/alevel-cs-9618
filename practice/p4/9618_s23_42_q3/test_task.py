import re
import runpy
import pytest
from testkit import run_script, use_files

def field(obj, name):
    for key, value in vars(obj).items():
        if key == name or key.endswith("__"+name): return value
    raise AssertionError(name)

def test_3a_i_ii_employee_initial_state(sol):
    """9618_s23_42:3(a)(i) MP2, MP4-MP5; 3(a)(ii) MP2: 52 independent zero pays, ID preserved."""
    a=sol.Employee("00123",12.5,"Tester"); b=sol.Employee("00002",20.0,"Developer")
    assert a.GetEmployeeNumber() == "00123"
    assert field(a,"HourlyPay") == 12.5 and field(a,"JobTitle") == "Tester"
    assert field(a,"PayYear2022") == [0.0]*52
    a.SetPay(1,2)
    assert b.GetTotalPay() == 0

@pytest.mark.parametrize("week", [1,26,52])
def test_3a_iii_iv_set_week_and_total(sol, week):
    """9618_s23_42:3(a)(iii) MP2-MP3; 3(a)(iv) MP1-MP2: all 52 weeks, overwrite correct slot."""
    e=sol.Employee("00123",12.5,"Tester")
    e.SetPay(week,4)
    assert field(e,"PayYear2022")[week-1] == 50
    assert e.GetTotalPay() == 50
    e.SetPay(week,2)
    assert e.GetTotalPay() == 25

def test_3b_inherits_and_calls_parent_with_bonus(sol, monkeypatch):
    """9618_s23_42:3(b)(i) MP1, MP3-MP4; 3(b)(ii) MP2-MP3: percent increase and parent call."""
    assert issubclass(sol.Manager,sol.Employee)
    m=sol.Manager("02586",22.5,"Manager",5.25)
    calls=[]
    original=sol.Employee.SetPay
    def spy(self,week,hours): calls.append((week,hours)); return original(self,week,hours)
    monkeypatch.setattr(sol.Employee,"SetPay",spy)
    m.SetPay(52,28.5)
    assert calls == [(52,pytest.approx(29.99625))]
    assert m.GetTotalPay() == pytest.approx(674.915625)

def test_3c_load_employees(sol,candidate_path,exercise_dir,monkeypatch,tmp_path,capsys):
    """9618_s23_42:3(c) MP1, MP3-MP8: eight records, optional bonus, correct class/data."""
    use_files(monkeypatch,tmp_path,exercise_dir / "files")
    ns=runpy.run_path(str(candidate_path),run_name="__main__")
    employees=ns["EmployeeArray"]
    assert len(employees)==8
    assert [e.GetEmployeeNumber().strip() for e in employees] == ["12452","21548","02586","65912","42004","82610","51947","51847"]
    manager=type(employees[2])
    assert issubclass(manager,type(employees[0])) and manager is not type(employees[0])
    assert [type(e) is manager for e in employees] == [False,False,True,False,True,False,True,True]
    assert [e.GetTotalPay() for e in employees] == pytest.approx([730.56,890,674.915625,475,768.5955,502.075,1216.1409,339.5925])

def test_3d_enterhours_matches_ids(sol,exercise_dir,monkeypatch,tmp_path):
    """9618_s23_42:3(d) MP1, MP3-MP6: pair reading, linear search by getter, dispatch SetPay."""
    use_files(monkeypatch,tmp_path,exercise_dir / "files")
    ids=["51847","42004","65912","02586","82610","51947","12452","21548"]
    class Employee:
        def __init__(self, id): self.id,self.calls=id,[]
        def GetEmployeeNumber(self): return self.id
        def SetPay(self,week,hours): self.calls.append((week,hours))
    sol.EmployeeArray=[Employee(id) for id in ids]
    sol.EnterHours()
    assert [e.calls for e in sol.EmployeeArray] == [[(1,h)] for h in [10.0,22.5,38,28.5,47.5,51,48,50]]

def test_3d_missing_hours(sol,monkeypatch,tmp_path,capsys):
    """9618_s23_42:3(d) MP2: missing hours file produces an exception message."""
    monkeypatch.chdir(tmp_path)
    sol.EnterHours()
    assert capsys.readouterr().out.strip()

def test_3c_missing_employees(candidate_path,exercise_dir,monkeypatch,tmp_path,capsys):
    """9618_s23_42:3(c) MP2: exception message; EnterHours is stopped before undefined follow-up."""
    import sys
    monkeypatch.chdir(tmp_path)
    class Stop(Exception): pass
    def trace(frame,event,arg):
        if frame.f_code.co_name=="EnterHours" and event=="call": raise Stop
        return trace
    previous=sys.gettrace()
    try:
        sys.settrace(trace)
        try: runpy.run_path(str(candidate_path),run_name="__main__")
        except Stop: pass
    finally: sys.settrace(previous)
    assert capsys.readouterr().out.strip()

def test_3e_ii_screenshot_all_pays(candidate_path,exercise_dir):
    """9618_s23_42:3(e)(i) MP1-MP2; 3(e)(ii) whole: eight ID/pay pairs from MS p.37."""
    result=run_script(candidate_path,files_dir=exercise_dir / "files")
    assert result.returncode == 0,result.stderr
    numbers=re.findall(r"\d+(?:\.\d+)?",result.stdout)
    pairs={numbers[i]:float(numbers[i+1]) for i in range(0,len(numbers),2)}
    assert pairs == pytest.approx({"12452":730.56,"21548":890,"02586":674.915625,"65912":475,"42004":768.5955,"82610":502.075,"51947":1216.1409,"51847":339.5925},rel=1e-6)
