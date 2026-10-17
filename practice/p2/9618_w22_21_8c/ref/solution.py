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
    ErrCount=0
    if not CheckFile(ThisFile):
        print('That program file is not valid')
        return
    with open(ThisFile,encoding='utf-8') as Handle:
        for RawLine in Handle:
            if CheckLine(RawLine.rstrip('\n'))!=0:
                ErrCount+=1
            if ErrCount>MaxErrors:
                print('Check terminated - too many errors')
                return
    print('There were '+str(ErrCount)+' errors.')
