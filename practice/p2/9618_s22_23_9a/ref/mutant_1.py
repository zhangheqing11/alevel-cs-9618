# 9618_s22_23:9(a) MP5: input-validation
import random,string
# Provided modules matching the QP contract.
def RandomChar():
    return random.choice(string.ascii_letters+string.digits)

def Exists(ThisString, Search):
    for c in ThisString:
        if c == Search:
            return True
    return False

def Generate():
    Password = ''
    for ACount in range(3):
        Group = ''
        for BCount in range(4):
            NextChar = RandomChar()
            while False:
                NextChar = RandomChar()
            Group += NextChar
        Password += Group + '-'
    return Password[:-1]
