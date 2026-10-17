def FindBaseNumber(ThisValue):
    Num=0
    Try=1
    while Try<=ThisValue:
        Num+=1
        Try*=Num
        if Try==ThisValue:
            return Num
    return -1
