def LastLines(ThisFile):
    LineY=''
    LineZ=''
    with open(ThisFile,encoding='utf-8') as Handle:
        for ThisLine in Handle:
            LineX=LineY
            LineY=LineZ
            LineZ=ThisLine.rstrip('\n')
    print(LineX)
    print(LineY)
    print(LineZ)
