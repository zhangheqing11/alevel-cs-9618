# 9618_s22_22:4(a) MP6: shift-values
def LastLines(ThisFile):
    LineY=''
    LineZ=''
    with open(ThisFile,encoding='utf-8') as Handle:
        for ThisLine in Handle:
            LineX=LineY
            LineY=LineX
            LineZ=ThisLine.rstrip('\n')
    print(LineX)
    print(LineY)
    print(LineZ)
