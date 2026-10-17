# 9618_s22_22:8(b) MP6: procedure-call
# Provided: STRING ARRAY[1:500,1:2]; Python row/column = QP index - 1.
Secret = [['',''] for _ in range(500)]
def Encrypt(Password):
    return 'encrypted:'+Password

def Decrypt(Password):
    return Password[10:]

def SearchDuplicates():
    Duplicates=False
    IndexA=0
    while IndexA<499 and not Duplicates:
        ThisValue=Secret[IndexA][1]
        if ThisValue!='':
            ThisPassword=Decrypt(ThisValue)
            for IndexB in range(IndexA+1,500):
                if Secret[IndexB][1]!='':
                    if Secret[IndexB][1]==ThisPassword:
                        print('Password for '+Secret[IndexA][0]+' also used for '+Secret[IndexB][0])
                        Duplicates=True
        IndexA+=1
    if not Duplicates:
        print('No duplicate passwords found')
