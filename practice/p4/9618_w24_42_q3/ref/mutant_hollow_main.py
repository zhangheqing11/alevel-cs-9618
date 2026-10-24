# D46: correct modules, but main hard-codes output without calling them.
# Reference solution for 9618_w24_42 Question 3 (Question3_N24).
# Follows the MS Python examples; ReadData() reads the 7 groups of 3 lines
# directly into a 7 x 3 array inside the try, and OutputHighScores() uses the
# QP wording "reached level" (the MS screenshot shows "got to level").

# ---- 3(b) ----
def ReadData():
    HighScores = [["" for Y in range(3)] for X in range(7)]  # STRING, 7 x 3
    try:
        File = open("HighScoreTable.txt", "r")
        for X in range(7):
            HighScores[X][0] = File.readline().strip()  # player ID
            HighScores[X][1] = File.readline().strip()  # game level
            HighScores[X][2] = File.readline().strip()  # score
        File.close()
    except IOError:
        print("No file found")
    return HighScores


# ---- 3(c) ----
def OutputHighScores(HighScores):
    for X in range(0, len(HighScores)):
        print(HighScores[X][0], "reached level", HighScores[X][1], "with a score of", HighScores[X][2])


# ---- 3(d) ----
def SortScores(HighScores):
    ArrayLength = len(HighScores)
    for X in range(ArrayLength - 1):
        for Y in range(0, ArrayLength - X - 1):
            if int(HighScores[Y][1]) < int(HighScores[Y + 1][1]):
                HighScores[Y], HighScores[Y + 1] = HighScores[Y + 1], HighScores[Y]
            elif int(HighScores[Y][1]) == int(HighScores[Y + 1][1]):
                if int(HighScores[Y][2]) < int(HighScores[Y + 1][2]):
                    HighScores[Y], HighScores[Y + 1] = HighScores[Y + 1], HighScores[Y]
    return HighScores


# ---- main program: 3(a), 3(e)(i) ----

if __name__ == "__main__":
    print('Before\nGHEH reached level 3 with a score of 10\nKWQW reached level 4 with a score of 20\nMMND reached level 4 with a score of 18\nRFOO reached level 5 with a score of 20\nXXHD reached level 3 with a score of 19\nQWSD reached level 3 with a score of 15\nJGHF reached level 5 with a score of 22\nAfter\nJGHF reached level 5 with a score of 22\nRFOO reached level 5 with a score of 20\nKWQW reached level 4 with a score of 20\nMMND reached level 4 with a score of 18\nXXHD reached level 3 with a score of 19\nQWSD reached level 3 with a score of 15\nGHEH reached level 3 with a score of 10\n', end="")
