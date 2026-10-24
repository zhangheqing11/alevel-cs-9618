# Mutant: 9618_w23_42:2(a)(i) MP3 (div-mod) - MODULUS operands reversed (Number MOD ToFind).
# Reference solution for 9618_w23_42 Question 2 (Question2_N23).
# Same as the MS Python examples (MS p.18 and p.20).

# ---- 2(a)(i) ----
def IterativeCalculate(Number):  # Number : INTEGER, returns INTEGER
    Total = 0
    ToFind = Number
    while Number != 0:
        if Number % ToFind == 0:
            Total = Total + Number
        Number = Number - 1
    return Total


# ---- 2(b)(i) ----
def RecursiveValue(Number, ToFind):  # Number, ToFind : INTEGER, returns INTEGER
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)


# ---- main program: 2(a)(ii), 2(b)(ii) ----
if __name__ == "__main__":
    print(IterativeCalculate(10))
    print(RecursiveValue(50, 50))
