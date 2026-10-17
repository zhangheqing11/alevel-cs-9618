def Unpack(TLine,SID,SDesc,SCost):
    SID[0]=TLine[:5]
    SDesc[0]=TLine[5:37]
    SCost[0]=TLine[37:]
