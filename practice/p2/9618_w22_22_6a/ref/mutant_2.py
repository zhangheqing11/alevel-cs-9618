# 9618_w22_22:6(a) MP8: return-value
def FindBaseNumber(ThisValue):
    Num=0
    Try=1
    while Try<=ThisValue:
        Num+=1
        Try*=Num
        if Try==ThisValue:
            return Num
    return Num
