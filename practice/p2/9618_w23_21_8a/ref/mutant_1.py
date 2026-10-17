# 9618_w23_21:8(a) MP5: string-concat
# Provided environment and transport; tests replace Transmit with a recorder.
MyID='101'
def Transmit(Message,Port):
    pass

def SendFile(FileName,DestID,Port):
    with open(FileName,encoding='utf-8') as Handle:
        for RawLine in Handle:
            FileData=RawLine.rstrip('\n')
            Transmit(chr(2)+MyID+DestID+FileData+chr(3),Port)
    Transmit(chr(2)+DestID+MyID+'****'+chr(3),Port)
