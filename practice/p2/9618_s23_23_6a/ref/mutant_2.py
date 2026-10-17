# 9618_s23_23:6(a) MP7: div-mod
def Select(Start, End):
    for ThisNum in range(Start+1,End):
        ThisString=str(ThisNum)
        Char1=ThisString[-1]
        Char2=ThisString[-2]
        Total=int(Char1)*int(Char2)
        if Total==6:
            print(ThisNum)
