# 9618_s23_21:4 MP4: char-compare
def Replace(OldString, Char1, Char2):
    NewString = ''
    for ThisChar in OldString:
        if ThisChar.upper() == Char1.upper():
            ThisChar = Char2
        NewString += ThisChar
    return NewString
