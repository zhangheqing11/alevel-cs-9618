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
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
