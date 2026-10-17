# 9618_s23_21:3(b) MP3: relational-ops.


def main():
    Amount = float(input("Amount: "))
    if Amount < 10:
        Rate = 5
    elif Amount < 100:
        Rate = 7
    else:
        Rate = 10
    Points = int(Amount) * Rate
    print(Points)
