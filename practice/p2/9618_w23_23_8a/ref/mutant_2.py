# 9618_w23_23:8(a) MP6: file-write
# Provided receiver: tests inject a finite sequence, never wait on a real network.
def GetData():
    return '****'

def ReceiveFile(FileName):
    CharCount=0
    with open(FileName,'w',encoding='utf-8') as Handle:
        FileData=GetData()
        while FileData!='****':
            Handle.write('****\n')
            CharCount+=len(FileData)
            FileData=GetData()
    print(str(CharCount)+' characters were written to '+FileName)
