# 9618_s23_22:6 MP7: boundary-values
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
    if Dim != 0:
        print(StringA)
