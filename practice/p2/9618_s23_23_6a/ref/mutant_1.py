# 9618_s23_23:6(a) MP3: loop-bounds
def Select(Start, End):
    for ThisNum in range(Start,End+1):
        ThisString=str(ThisNum)
        Char1=ThisString[-1]
        Char2=ThisString[-2]
        Total=int(Char1)+int(Char2)
        if Total==6:
            print(ThisNum)
