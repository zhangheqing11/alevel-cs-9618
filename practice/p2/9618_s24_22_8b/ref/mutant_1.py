# 9618_s24_22:8(b) MP3: char-compare
def DeleteSpaces(Line):
    Count=0
    while Count<len(Line):
        if Line[Count]==' ':
            return Line[Count:]
        Count+=1
    return ''
