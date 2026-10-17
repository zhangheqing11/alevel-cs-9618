# 9618_w22_23:3 MP3: accumulator.


def main():
    SumPos = 0.0
    SumNeg = 0.0
    Number = float(input("Number: "))
    while Number != 0:
        if Number > 0:
            SumPos += Number
        else:
            SumPos += Number
        Number = float(input("Number: "))
    print(SumPos)
    print(SumNeg)
