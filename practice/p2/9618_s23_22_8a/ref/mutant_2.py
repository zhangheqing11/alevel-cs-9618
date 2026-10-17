# 9618_s23_22:8(a) MP1: input-validation
# Provided module from the QP; alphabetic means the ASCII letter ranges.
def OnlyAlpha(Text):
    for c in Text:
        if not ('A'<=c<='Z' or 'a'<=c<='z'):
            return False
    return True

def CheckInfo(NewLine):
    if len(NewLine)<18:
        return False
    for c in NewLine[:4]:
        if c<'0' or c>'9':
            return False
    ThisNum=NewLine[:4]
    if ThisNum<'0001' or ThisNum>'5999':
        return False
    if not OnlyAlpha(NewLine[4:7]):
        return False
    return True
