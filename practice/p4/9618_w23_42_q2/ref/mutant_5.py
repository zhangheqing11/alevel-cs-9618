# Mutant: 9618_w23_42:2(b)(i) MP2 (recursion) - RecursiveValue written as a loop, no recursive calls.
# Reference solution for 9618_w23_42 Question 2 (Question2_N23).
# Same as the MS Python examples (MS p.18 and p.20).

# ---- 2(a)(i) ----
def IterativeCalculate(Number):  # Number : INTEGER, returns INTEGER
    Total = 0
    ToFind = Number
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        Number = Number - 1
    return Total


# ---- 2(b)(i) ----
def RecursiveValue(Number, ToFind):  # Number, ToFind : INTEGER, returns INTEGER
    Total = 0
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        Number = Number - 1
    return Total


# ---- main program: 2(a)(ii), 2(b)(ii) ----
if __name__ == "__main__":
    print(IterativeCalculate(10))
    print(RecursiveValue(50, 50))
