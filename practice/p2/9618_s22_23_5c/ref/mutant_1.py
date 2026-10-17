# 9618_s22_23:5(c) MP4: boundary-values
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
    for Index in range(500):
        if Staff[Index].EmployeeNumber!=-1:
            if Staff[Index].Attendance<90:
                print(Staff[Index].EmployeeNumber)
                print(Staff[Index].Name)
