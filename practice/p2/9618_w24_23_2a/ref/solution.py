def main():
    Total=0
    for Count in range(100):
        NextNumber=int(input('Input an integer value: '))
        if NextNumber>0:
            Total+=NextNumber
    print(Total)
