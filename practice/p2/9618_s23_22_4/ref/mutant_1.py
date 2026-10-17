# 9618_s23_22:4 MP4: char-compare
def GetNum(ThisString, ThisChar):
    Count = 0
    for c in ThisString:
        if c.upper() == ThisChar.upper():
            Count += 1
    return Count
