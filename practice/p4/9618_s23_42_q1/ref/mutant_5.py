# MUTANT 9618_s23_42:1(d)(i) MP1 (procedure-call): main program forgets to call SortDescending().
# Question1_J2023 -- reference solution (close to the MS Python example)

# ---- 1(a) ----
# Animals: global array of 10 elements of type STRING
Animals = [""] * 10


# ---- 1(c) ----
def SortDescending():
    ArrayLength = len(Animals)
    for X in range(0, ArrayLength - 1):
        for Y in range(0, ArrayLength - X - 1):
            if Animals[Y][0:1] < Animals[Y + 1][0:1]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y + 1]
                Animals[Y + 1] = Temp


# ---- main program ----
if __name__ == "__main__":
    # 1(b)
    Animals[0] = "horse"
    Animals[1] = "lion"
    Animals[2] = "rabbit"
    Animals[3] = "mouse"
    Animals[4] = "bird"
    Animals[5] = "deer"
    Animals[6] = "whale"
    Animals[7] = "elephant"
    Animals[8] = "kangaroo"
    Animals[9] = "tiger"
    # 1(d)(i)
    for X in range(0, 10):
        print(Animals[X])
