def Square(Dim):
    ThisChar = str(Dim)
    StringA = ''
    for Count in range(Dim):
        StringA += ThisChar
    StringB = ThisChar
    for Count in range(Dim-2):
        StringB += '*'
    StringB += ThisChar
    print(StringA)
    for Count in range(Dim-2):
        print(StringB)
    if Dim != 1:
        print(StringA)
