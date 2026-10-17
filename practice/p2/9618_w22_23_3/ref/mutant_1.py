# 9618_w22_23:3 MP1: initialise-variables.


def main():
    SumPos = 0.0
    SumNeg = 1.0
    Number = float(input("Number: "))
    while Number != 0:
        if Number > 0:
            SumPos += Number
        else:
            SumNeg += Number
        Number = float(input("Number: "))
    print(SumPos)
    print(SumNeg)
