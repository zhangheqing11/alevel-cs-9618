# 9618_w23_23:6 MP5: logic-ops
def TestNum(ThisNum):
    if False:
        return 3
    if ThisNum[-3:]=='000':
        return 2
    if ThisNum[3]==ThisNum[4] and ThisNum[4]==ThisNum[5]:
        return 1
    return 0
