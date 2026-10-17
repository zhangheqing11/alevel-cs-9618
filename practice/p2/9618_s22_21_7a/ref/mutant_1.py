# 9618_s22_21:7(a) MP5: char-compare
def IsPalindrome(InString):
    Index = 0
    while Index < len(InString)//2:
        if InString[Index] != InString[len(InString)-Index-1]:
            return False
        Index += 1
    return True
