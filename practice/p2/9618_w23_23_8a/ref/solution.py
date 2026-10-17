# Provided receiver: tests inject a finite sequence, never wait on a real network.
def GetData():
    return '****'

def ReceiveFile(FileName):
    CharCount=0
    with open(FileName,'w',encoding='utf-8') as Handle:
        FileData=GetData()
        while FileData!='****':
            Handle.write(FileData+'\n')
            CharCount+=len(FileData)
            FileData=GetData()
    print(str(CharCount)+' characters were written to '+FileName)
