# 9618_w23_23:8(a) MP5: accumulator
# Provided receiver: tests inject a finite sequence, never wait on a real network.
def GetData():
    return '****'

def ReceiveFile(FileName):
    CharCount=0
    with open(FileName,'w',encoding='utf-8') as Handle:
        FileData=GetData()
        while FileData!='****':
            Handle.write(FileData+'\n')
            CharCount+=len(FileData)+1
            FileData=GetData()
    print(str(CharCount)+' characters were written to '+FileName)
