# 9618_s23_23:8(a) MP7: count-increment
def ChangeSupp(Code1,Code2):
    Count=0
    with open('Stock.txt',encoding='utf-8') as Source,open('NewStock.txt','w',encoding='utf-8') as Target:
        for RawLine in Source:
            ThisLine=RawLine.rstrip('\n')
            if ThisLine[4:7]==Code1:
                ThisLine=ThisLine[:4]+Code2+ThisLine[7:]
                Count+=0
            Target.write(ThisLine+'\n')
    return Count
