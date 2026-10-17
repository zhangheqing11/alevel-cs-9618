# 9618_s22_22:8(a) MP1: loop-bounds
# STRING array, 500 rows x 2 columns; Python indices = pseudocode indices - 1.
Secret = [["", ""] for _ in range(500)]

def Exists(ThisString, Search):
    Index = 0
    while Index < len(ThisString)-1:
        if ThisString[Index] == Search:
            return True
        Index += 1
    return False
