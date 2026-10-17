# Provided modules. CheckLine is a replaceable demonstration checker, not a full parser.
def CheckFile(ThisFile):
    Count=0
    with open(ThisFile,encoding='utf-8') as Handle:
        for RawLine in Handle:
            if RawLine.rstrip('\n')!='':
                Count+=1
                if Count>=10:
                    return True
    return False

def CheckLine(Line):
    return 1 if Line.startswith('ERROR') else 0

def CountErrors(ThisFile,MaxErrors):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
