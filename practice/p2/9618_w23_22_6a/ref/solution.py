def CreateFiles(NameRoot,NumFiles):
    for Count in range(1,NumFiles+1):
        FileName=NameRoot+'.'+str(Count).zfill(3)
        with open(FileName,'w',encoding='utf-8') as Handle:
            Handle.write('This is File '+FileName+'\n')
