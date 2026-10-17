def DeleteSpaces(Line):
    Count=0
    while Count<len(Line):
        if Line[Count]!=' ':
            return Line[Count:]
        Count+=1
    return ''
