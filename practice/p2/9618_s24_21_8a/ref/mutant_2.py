# 9618_s24_21:8(a) MP4: char-compare
def DeleteComment(Line):
    Count=0
    while Count<len(Line)-1:
        if Line[Count:Count+1]=='/':
            return Line[:Count]
        Count+=1
    return Line
