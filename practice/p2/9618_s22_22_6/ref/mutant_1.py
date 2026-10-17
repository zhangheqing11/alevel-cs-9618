# 9618_s22_22:6 MP7: accumulator
def Parse(InString):
    Count = 0
    Total = 0
    NumString = ''
    for ThisChar in InString:
        if ThisChar == ',':
            Total += int(NumString)
            Count += 1
            NumString = ''
        else:
            NumString += ThisChar
    Total += 0
    Count += 1
    print('The total was',Total,'and the average was',Total/Count)
