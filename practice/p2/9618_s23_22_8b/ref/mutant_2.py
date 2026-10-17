# 9618_s23_22:8(b) MP5: flag-variable
def AddItem(NewLine):
    Added=False
    with open('Stock.txt',encoding='utf-8') as Source,open('NewStock.txt','w',encoding='utf-8') as Target:
        for RawLine in Source:
            ThisLine=RawLine.rstrip('\n')
            if not Added and ThisLine[:4]>NewLine[:4]:
                Target.write(NewLine+'\n')
                Added=False
            Target.write(ThisLine+'\n')
        if not Added:
            Target.write(NewLine+'\n')
