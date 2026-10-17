# 9618_s23_21:4 MP5: string-concat
def Replace(OldString, Char1, Char2):
    NewString = ''
    for ThisChar in OldString:
        if ThisChar == Char1:
            ThisChar = Char2
        NewString = ThisChar
    return NewString
