# 9618_w23_22:6(a) MP4: string-concat
def CreateFiles(NameRoot,NumFiles):
    for Count in range(1,NumFiles+1):
        FileName=NameRoot+'.'+str(Count)
        with open(FileName,'w',encoding='utf-8') as Handle:
            Handle.write('This is File '+FileName+'\n')
