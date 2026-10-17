# 9618_w23_23:6 MP2: char-compare
def TestNum(ThisNum):
    if ThisNum[:3]==ThisNum[-3:]:
        return 3
    if ThisNum[-3:]=='000':
        return 2
    if ThisNum[4]==ThisNum[5]:
        return 1
    return 0
