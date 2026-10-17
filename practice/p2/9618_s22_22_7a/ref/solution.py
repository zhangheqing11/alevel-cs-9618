def MID(InString, Start, Num):
    Tail = InString[-(len(InString)-Start+1):]
    return Tail[:Num]
