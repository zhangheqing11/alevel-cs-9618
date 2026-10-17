# 9618_s24_23:8(b) MP7: array-2d
# Provided Header module; sample capacity (QP only requires sufficient rows).
# QP gives no total capacity; 11 illustrative STRING rows hold its two examples.
# Python indices = pseudocode indices - 1; Header does not access ModInfo.
ModInfo = [["", "", ""] for _ in range(11)]
ModInfo[9] = ["27", "P", "MyProc(Z : CHAR)"]
ModInfo[10] = ["35", "F", "MyFun(Y : CHAR) RETURNS BOOLEAN"]

def Header(Line):
    if len(Line)>=13:
        if Line[:9].upper()=='FUNCTION ':
            return 'F'+Line[9:]
        if Line[:10].upper()=='PROCEDURE ':
            return 'P'+Line[10:]
    return ''

ModInfo=[['','',''] for _ in range(100)]

def FindModules(FileName):
    Index=0
    LineNum=0
    with open(FileName,encoding='utf-8') as Handle:
        for RawLine in Handle:
            LineNum+=1
            Line=Header(RawLine.rstrip('\n'))
            if Line!='':
                ModInfo[Index][0]=str(LineNum)
                ModInfo[Index][1]=Line[0]
                ModInfo[Index][2]=Line[2:]
                Index+=1
