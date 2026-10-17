# 9618_w23_21:2(a) MP5: loop-bounds.


def main():
    Total = 0
    for Count in range(99):
        Number = float(input("Number: "))
        if Number >= 30 and Number <= 70:
            Total += Number
    print(Total)
