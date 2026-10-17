# 9618_s24_21:8(a) MP2: linear-search
def DeleteComment(Line):
    Count=0
    while Count<len(Line)-1:
        if Line[Count:Count+2]=='//':
            return Line[:Count+2]
        Count+=1
    return Line
