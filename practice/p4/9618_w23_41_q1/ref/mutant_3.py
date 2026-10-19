# Mutant: 9618_w23_41:1(b)(i) MP1 (recursion) - RecursiveVowels written with a loop, no recursive call.
# Reference solution for 9618_w23_41 Question 1 (Question1_N23).
# Follows the MS Python examples (MS p.6 and p.8); keeps LengthString from the
# given pseudocode so the loop runs LENGTH(Value) times.

# ---- 1(a)(i) ----
def IterativeVowels(Value):  # Value : STRING, returns INTEGER
    Total = 0
    LengthString = len(Value)
    for X in range(0, LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or \
                FirstCharacter == 'o' or FirstCharacter == 'u':
            Total = Total + 1
        Value = Value[1:len(Value)]
    return Total


# ---- 1(b)(i) ----
def RecursiveVowels(Value):  # Value : STRING, returns INTEGER
    Total = 0
    for Character in Value:
        if Character == 'a' or Character == 'e' or Character == 'i' or Character == 'o' or Character == 'u':
            Total = Total + 1
    return Total


# ---- main program: 1(a)(ii), 1(b)(ii) ----
if __name__ == "__main__":
    print(IterativeVowels("house"))
    print(RecursiveVowels("imagine"))
