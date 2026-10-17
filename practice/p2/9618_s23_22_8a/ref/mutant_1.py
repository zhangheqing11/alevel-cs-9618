# 9618_s23_22:8(a) MP4: relational-ops
# Provided module from the QP; alphabetic means the ASCII letter ranges.
def OnlyAlpha(Text):
    for c in Text:
        if not ('A'<=c<='Z' or 'a'<=c<='z'):
            return False
    return True

def CheckInfo(NewLine):
    if len(NewLine)<19:
        return False
    for c in NewLine[:4]:
        if c<'0' or c>'9':
            return False
    ThisNum=NewLine[:4]
    if ThisNum<'0001' or ThisNum>'6000':
        return False
    if not OnlyAlpha(NewLine[4:7]):
        return False
    return True
