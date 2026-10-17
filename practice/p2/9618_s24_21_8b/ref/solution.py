# Provided module from part (a).
def DeleteComment(Line):
    Count=0
    while Count<len(Line)-1:
        if Line[Count:Count+2]=='//':
            return Line[:Count]
        Count+=1
    return Line

def Stage_1(StudentName):
    Count=0
    with open(StudentName+'_src.txt',encoding='utf-8') as Source,open(StudentName+'_S1.txt','w',encoding='utf-8') as Target:
        for RawLine in Source:
            Line=DeleteComment(RawLine.rstrip('\n'))
            if Line!='':
                Target.write(Line+'\n')
                Count+=1
    return Count
