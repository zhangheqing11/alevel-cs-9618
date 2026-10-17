# 9618_s23_22:6 MP6: loop-bounds
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
    for Count in range(Dim-3):
        print(StringB)
    if Dim != 1:
        print(StringA)
