# 9618_w23_22:6(a) MP2: loop-bounds
def CreateFiles(NameRoot,NumFiles):
    for Count in range(1,NumFiles):
        FileName=NameRoot+'.'+str(Count).zfill(3)
        with open(FileName,'w',encoding='utf-8') as Handle:
            Handle.write('This is File '+FileName+'\n')
