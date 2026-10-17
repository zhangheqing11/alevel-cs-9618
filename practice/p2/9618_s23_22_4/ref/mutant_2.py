# 9618_s23_22:4 MP5: accumulator
def GetNum(ThisString, ThisChar):
    Count = 0
    for c in ThisString:
        if c == ThisChar:
            Count = 1
    return Count
