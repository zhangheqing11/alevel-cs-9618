# 9618_w22_23:5(a)(i) MP4: field-extract
def Unpack(TLine,SID,SDesc,SCost):
    SID[0]=TLine[:5]
    SDesc[0]=TLine[6:37]
    SCost[0]=TLine[37:]
