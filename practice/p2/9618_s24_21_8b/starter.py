# Provided module from part (a).
def DeleteComment(Line):
    Count=0
    while Count<len(Line)-1:
        if Line[Count:Count+2]=='//':
            return Line[:Count]
        Count+=1
    return Line

def Stage_1(StudentName):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
