# 9618_w22_22:4(a) MP5: nested-if.
# Provided external array; the diagram only accesses QP indices 4, 5, 6.
# Six REAL locations suffice here. Python index = QP index - 1.
SameMonth = [0.0] * 6


def GetAverage(UserID):
    return 0.0


def Update(UserID, Total):
    pass


def main():
    UserID = input("UserID: ")
    Average = GetAverage(UserID)
    Total = 0
    Index = 4
    while Index < 7:
        Last = SameMonth[Index - 1]
        if Average < Last:
            Total += Average
        else:
            Total += Last
        Index += 1
    Update(UserID, Total)
