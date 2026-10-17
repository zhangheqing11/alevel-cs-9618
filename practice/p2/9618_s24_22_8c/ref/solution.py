# Provided modules.
def DeleteComment(Line):
    Count=0
    while Count<len(Line)-1:
        if Line[Count:Count+2]=='//':
            return Line[:Count]
        Count+=1
    return Line

def DeleteSpaces(Line):
    Count=0
    while Count<len(Line):
        if Line[Count]!=' ':
            return Line[Count:]
        Count+=1
    return ''

def Stage_2(F1,F2):
    Count=0
    with open(F1,encoding='utf-8') as Source,open(F2,'a',encoding='utf-8') as Target:
        for RawLine in Source:
            Line=DeleteComment(DeleteSpaces(RawLine.rstrip('\n')))
            if Line!='':
                Target.write(Line+'\n')
            else:
                Count+=1
    print(str(Count)+' blank lines were removed')
