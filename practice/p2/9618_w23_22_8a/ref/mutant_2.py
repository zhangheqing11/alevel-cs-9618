# 9618_w23_22:8(a) MP3: array-2d
# Provided INTEGER ARRAY[1:6,1:3], QP example; Python row/column = QP - 1.
# Unused row's last two values are arbitrary integers, not meaningful defaults.
RouteTable=[[100,199,1],[200,259,2],[-1,0,0],[260,399,2],[400,599,3],[600,999,1]]

def GetPort(ThisDest):
    DNum=int(ThisDest)
    for Index in range(5):
        if RouteTable[Index][0]!=-1:
            if DNum>=RouteTable[Index][0] and DNum<=RouteTable[Index][1]:
                return RouteTable[Index][2]
    return -1
