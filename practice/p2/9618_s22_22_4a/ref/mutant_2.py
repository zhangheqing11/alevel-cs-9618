# 9618_s22_22:4(a) MP2: file-close
def LastLines(ThisFile):
    LineY=''
    LineZ=''
    if True:
        Handle=open(ThisFile,encoding='utf-8')
        for ThisLine in Handle:
            LineX=LineY
            LineY=LineZ
            LineZ=ThisLine.rstrip('\n')
    print(LineX)
    print(LineY)
    print(LineZ)
