# 9618_s24_22:8(b) MP5: string-functions
def DeleteSpaces(Line):
    Count=0
    while Count<len(Line):
        if Line[Count]!=' ':
            return Line[Count+1:]
        Count+=1
    return ''
