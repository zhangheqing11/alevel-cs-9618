def Factorial(ThisNum):
    if ThisNum < 0:
        return -1
    Value = 1
    while ThisNum != 0:
        Value *= ThisNum
        ThisNum -= 1
    return Value
