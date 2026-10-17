# 9618_w22_21:8(a) MP7: relational-ops
def CheckFile(ThisFile):
    Count=0
    with open(ThisFile,encoding='utf-8') as Handle:
        for RawLine in Handle:
            if RawLine.rstrip('\n')!='':
                Count+=1
                if Count>10:
                    return True
    return False
