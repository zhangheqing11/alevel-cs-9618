def CheckNumber(Number):
    Total=0
    NumString=str(Number)
    CheckDigit=int(NumString[-1])
    for Index in range(len(NumString)-1):
        Total+=int(NumString[Index])
    return Total%10==CheckDigit
