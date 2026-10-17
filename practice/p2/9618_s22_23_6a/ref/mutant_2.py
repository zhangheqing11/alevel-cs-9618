# 9618_s22_23:6(a) MP2: initialise-variables
def Factorial(ThisNum):
    if ThisNum < 0:
        return -1
    Value = 0
    while ThisNum != 0:
        Value *= ThisNum
        ThisNum -= 1
    return Value
