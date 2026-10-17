from testkit import output_lines

def test_used_records_threshold_and_final_slot(sol,capsys):
    """9618_s22_23:5(c) MP2,3,4,5; behaviour (syntax and declarations checked manually)."""
    sol.Staff[0]=sol.Employee(1,'First',Attendance=90.0)
    sol.Staff[1]=sol.Employee(2,'Not absent',Attendance=90.1)
    sol.Staff[2]=sol.Employee(-1,'Unused',Attendance=0.0)
    sol.Staff[499]=sol.Employee(500,'Last',Attendance=89.9)
    sol.Absentees()
    assert output_lines(capsys.readouterr().out)==['1','First','500','Last']

def test_no_absentees(sol,capsys):
    """9618_s22_23:5(c) MP2,3,4,5; behaviour (syntax and declarations checked manually)."""
    sol.Absentees()
    assert capsys.readouterr().out==''
