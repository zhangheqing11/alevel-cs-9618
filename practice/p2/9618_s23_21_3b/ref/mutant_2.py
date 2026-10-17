# 9618_s23_21:3(b) MP4: type-conversion.


def main():
    Amount = float(input("Amount: "))
    if Amount < 10:
        Rate = 5
    elif Amount <= 100:
        Rate = 7
    else:
        Rate = 10
    Points = Amount * Rate
    print(Points)
