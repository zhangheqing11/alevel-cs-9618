# 9618_w23_21:8(a) MP7: procedure-call
# Provided environment and transport; tests replace Transmit with a recorder.
MyID='101'
def Transmit(Message,Port):
    pass

def SendFile(FileName,DestID,Port):
    with open(FileName,encoding='utf-8') as Handle:
        for RawLine in Handle:
            FileData=RawLine.rstrip('\n')
            Transmit(chr(2)+DestID+MyID+FileData+chr(3),Port)
    pass
