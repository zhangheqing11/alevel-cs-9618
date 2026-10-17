from datetime import date
# Provided record type; defaults here represent unused fixture records.
class Employee:
    def __init__(self,EmployeeNumber=-1,Name='',Department='',Born=date(2006,2,13),Attendance=100.0):
        self.EmployeeNumber=EmployeeNumber
        self.Name=Name
        self.Department=Department
        self.Born=Born
        self.Attendance=Attendance
# Employee ARRAY[1:500]; Python index = QP index - 1.
Staff=[Employee() for _ in range(500)]

def Absentees():
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
