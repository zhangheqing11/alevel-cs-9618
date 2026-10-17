# 9618_w25_23:6(b) MP4: loop-bounds
def CheckNumber(Number):
    Total=0
    NumString=str(Number)
    CheckDigit=int(NumString[-1])
    for Index in range(len(NumString)):
        Total+=int(NumString[Index])
    return Total%10==CheckDigit
