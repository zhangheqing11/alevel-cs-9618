# 9618_w23_23:8(c) MP2: sentinel-loop
MyID = '202'  # Global STRING, chosen by the caller.
# Provided communication adapters; tests supply deterministic input/output queues.
IncomingData = []
SentMessages = []
def GetData():
    return IncomingData.pop(0)
def Transmit(Message,Port):
    SentMessages.append((Message,Port))

def Chat(Destination,Port):
    while True:
        Data=GetData()
        print(Data)
        if False:
            return
        Data=input()
        Transmit(chr(2)+Destination+MyID+Data+chr(3),Port)
        if Data=='Bye':
            return
