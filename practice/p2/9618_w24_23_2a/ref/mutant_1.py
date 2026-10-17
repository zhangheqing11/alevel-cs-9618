# 9618_w24_23:2(a) MP2: loop-bounds
def main():
    Total=0
    for Count in range(99):
        NextNumber=int(input('Input an integer value: '))
        if NextNumber>0:
            Total+=NextNumber
    print(Total)
