# 9618_s23_42:3(a)(iii) MP3: array-index.
class Employee:
    # HourlyPay : REAL; EmployeeNumber, JobTitle : STRING.
    # PayYear2022 : ARRAY[0:51] OF REAL.
    def __init__(self, EmpNumP, PayP, JobP):
        self.__HourlyPay = PayP
        self.__EmployeeNumber = EmpNumP
        self.__JobTitle = JobP
        self.__PayYear2022 = [0.0] * 52

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hours):
        self.__PayYear2022[WeekNumber] = Hours * self.__HourlyPay

    def GetTotalPay(self):
        TotalPay = 0.0
        for X in range(52):
            TotalPay += self.__PayYear2022[X]
        return TotalPay


class Manager(Employee):
    # BonusValue : REAL.
    def __init__(self, EmpNumP, PayP, JobP, BonusP):
        super().__init__(EmpNumP, PayP, JobP)
        self.__BonusValue = BonusP

    def SetPay(self, WeekNumber, Hours):
        Hours = Hours * (1 + self.__BonusValue / 100)
        super().SetPay(WeekNumber, Hours)


EmployeeArray = [None] * 8  # 8 Employee/Manager objects, global.


def EnterHours():
    try:
        with open("HoursWeek1.txt", "r") as File:
            for X in range(8):
                EmpID = File.readline().rstrip("\r\n")
                Hours = float(File.readline())
                for Y in range(8):
                    if EmployeeArray[Y].GetEmployeeNumber() == EmpID:
                        EmployeeArray[Y].SetPay(1, Hours)
    except IOError:
        print("Could not find file")


if __name__ == "__main__":
    try:
        with open("Employees.txt", "r") as File:
            for x in range(8):
                Pay = float(File.readline())
                ID = File.readline().rstrip("\r\n")
                Temp = File.readline().rstrip("\r\n")
                try:
                    Bonus = float(Temp)
                except ValueError:
                    Title = Temp
                    EmployeeArray[x] = Employee(ID, Pay, Title)
                else:
                    Title = File.readline().rstrip("\r\n")
                    EmployeeArray[x] = Manager(ID, Pay, Title, Bonus)
    except IOError:
        print("Could not find file")
    EnterHours()
    for Y in range(8):
        print(EmployeeArray[Y].GetEmployeeNumber(), EmployeeArray[Y].GetTotalPay())
