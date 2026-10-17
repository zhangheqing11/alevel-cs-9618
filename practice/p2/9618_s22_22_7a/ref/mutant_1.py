# 9618_s22_22:7(a) MP2: string-index
def MID(InString, Start, Num):
    Tail = InString[-(len(InString)-Start):]
    return Tail[:Num]
