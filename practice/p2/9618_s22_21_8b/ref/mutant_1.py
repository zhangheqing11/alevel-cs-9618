# 9618_s22_21:8(b) MP2: loop-bounds
# Provided: STRING ARRAY[1:500,1:2]; Python row/column = QP index - 1.
Secret = [['',''] for _ in range(499)]
def Encrypt(Password):
    return 'encrypted:'+Password

def Decrypt(Password):
    return Password[10:]

def FindPassword(Name):
    for Index in range(500):
        if Secret[Index][0]==Name:
            return Decrypt(Secret[Index][1])
    print('Domain name not found')
    return ''
