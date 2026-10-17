# 9618_s22_22:7(a) MP3: string-functions
def MID(InString, Start, Num):
    Tail = InString[-(len(InString)-Start+1):]
    return Tail[:Num-1]
