from datetime import date

def test_employee_fields(sol):
    """9618_s22_23:5(a)(i) MP1,2,3,4; behaviour (syntax and declarations checked manually)."""
    employee=sol.Employee(123,'Smith,Eric','1B',date(2006,2,13),97.40)
    assert employee.EmployeeNumber==123 and type(employee.EmployeeNumber) is int
    assert employee.Name=='Smith,Eric' and employee.Department=='1B'
    assert employee.Born==date(2006,2,13) and type(employee.Born) is date
    assert employee.Attendance==97.40 and type(employee.Attendance) is float
