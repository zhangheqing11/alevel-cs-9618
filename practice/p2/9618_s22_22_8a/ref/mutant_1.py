# 9618_s22_22:8(a) MP3: char-compare
# STRING array, 500 rows x 2 columns; Python indices = pseudocode indices - 1.
Secret = [["", ""] for _ in range(500)]

def Exists(ThisString, Search):
    Index = 0
    while Index < len(ThisString):
        if ThisString[Index].upper() == Search.upper():
            return True
        Index += 1
    return False
