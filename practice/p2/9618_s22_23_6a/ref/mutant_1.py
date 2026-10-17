# 9618_s22_23:6(a) MP3: relational-ops
def Factorial(ThisNum):
    if ThisNum < 0:
        return 0
    Value = 1
    while ThisNum != 0:
        Value *= ThisNum
        ThisNum -= 1
    return Value
