def GetNum(ThisString, ThisChar):
    Count = 0
    for c in ThisString:
        if c == ThisChar:
            Count += 1
    return Count
