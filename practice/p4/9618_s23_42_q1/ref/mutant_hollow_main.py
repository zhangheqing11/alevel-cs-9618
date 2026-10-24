# D46: correct modules, but main hard-codes output without calling them.
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
    print('whale\ntiger\nrabbit\nmouse\nlion\nkangaroo\nhorse\nelephant\ndeer\nbird\n', end="")
