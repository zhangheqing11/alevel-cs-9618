# Provided lookup; the exercise dataset can be replaced by the tests.
ExistingSuppliers = ['ABCDE']
def SuppExists(Code):
    if len(Code) != 5:
        raise ValueError('Supplier code must contain five characters')
    for Supplier in ExistingSuppliers:
        if Supplier == Code:
            return True
    return False

def IsNewSupp(ThisString):
    if len(ThisString) != 5:
        return False
    if SuppExists(ThisString):
        return False
    for ThisChar in ThisString:
        if ThisChar.lower() < 'a' or ThisChar.lower() > 'z':
            return False
    return True
