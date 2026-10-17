# 9618_s22_23:9(b) MP2: loop-bounds
# Provided: STRING ARRAY[1:500,1:2]; Python row/column = QP index - 1.
Secret = [['',''] for _ in range(500)]
def Encrypt(Password):
    return 'encrypted:'+Password

def Decrypt(Password):
    return Password[10:]

def FindPassword(Name):
    for Index in range(500):
        if Secret[Index][0]==Name:
            return Decrypt(Secret[Index][1])
    return ''

def AddPassword(Name,Password):
    if FindPassword(Name)!='':
        return False
    for Index in range(499):
        if Secret[Index][0]=='':
            Secret[Index][0]=Name
            Secret[Index][1]=Encrypt(Password)
            return True
    return False
