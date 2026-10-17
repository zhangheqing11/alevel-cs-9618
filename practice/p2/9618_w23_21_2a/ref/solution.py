

def main():
    Total = 0
    for Count in range(100):
        Number = float(input("Number: "))
        if Number >= 30 and Number <= 70:
            Total += Number
    print(Total)
