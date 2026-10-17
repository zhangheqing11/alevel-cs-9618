# 9618_s22_21:7(a) MP6: loop-bounds
def IsPalindrome(InString):
    Index = 0
    while Index < max(0,len(InString)//2-1):
        if InString[Index].upper() != InString[len(InString)-Index-1].upper():
            return False
        Index += 1
    return True
