# 9618_w25_21:4(a) MP5: relational-ops
# Provided REAL ARRAY[1:20]; Python index = QP index - 1.
Number=[0.0]*20

def Store():
    LastNum=float(input('Value: '))
    Number[0]=LastNum
    Count=1
    while Count<20:
        ThisNum=float(input('Value: '))
        if ThisNum<LastNum:
            break
        Number[Count]=ThisNum
        LastNum=ThisNum
        Count+=1
    print(str(Count)+' values were stored in the array')
