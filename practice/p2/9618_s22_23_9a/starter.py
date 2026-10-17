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
    raise NotImplementedError
