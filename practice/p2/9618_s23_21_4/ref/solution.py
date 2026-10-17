def Replace(OldString, Char1, Char2):
    NewString = ''
    for ThisChar in OldString:
        if ThisChar == Char1:
            ThisChar = Char2
        NewString += ThisChar
    return NewString
