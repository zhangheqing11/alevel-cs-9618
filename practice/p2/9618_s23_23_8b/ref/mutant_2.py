# 9618_s23_23:8(b) MP4: count-increment
def Report_1(Supp):
    Count=0
    print('Report for Supplier: '+Supp)
    print('Item          Description')
    with open('Stock.txt',encoding='utf-8') as Handle:
        for RawLine in Handle:
            ThisLine=RawLine.rstrip('\n')
            if ThisLine[4:7]==Supp:
                print(ThisLine[:4]+'          '+ThisLine[7:])
                Count+=0
    print('Number of items listed: '+str(Count))
