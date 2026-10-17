def IsPalindrome(InString):
    Index = 0
    while Index < len(InString)//2:
        if InString[Index].upper() != InString[len(InString)-Index-1].upper():
            return False
        Index += 1
    return True
