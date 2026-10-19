# MUTANT 9618_s22_41:1(b) MP7-MP8 (exception-handling): no try/except, crashes when the file is missing.
# Question1_J2022 -- reference solution (close to the MS Python example, slips fixed)

# ---- 1(a) ----
# FileData: global 2D array, 11 elements x 2 fields (10 read from the file + 1 for the new player)
# FileData[x][0] = player name : STRING, FileData[x][1] = score : STRING (as read from the file)
FileData = [["", ""] for i in range(11)]


# ---- 1(b) ----
def ReadHighScores():
    Filename = "HighScore.txt"
    File = open(Filename, "r")
    for x in range(0, 10):
        FileData[x][0] = File.readline().strip()
        FileData[x][1] = File.readline().strip()
    File.close()


# ---- 1(c) ----
def OutputHighScores():
    for x in range(0, 11):
        Output = FileData[x][0] + " " + FileData[x][1]
        print(Output)


# ---- 1(e)(ii) ----
def Arrange(Username, Score):
    # Username : STRING, Score : INTEGER
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            # move elements x..9 down one place (element 10 receives the old 10th player)
            Count = 10
            while Count > x:
                FileData[Count][0] = FileData[Count - 1][0]
                FileData[Count][1] = FileData[Count - 1][1]
                Count = Count - 1
            FileData[x][0] = Username
            FileData[x][1] = str(Score)
            break


# ---- 1(f) ----
def WriteTopTen():
    Filename = "NewHighScore.txt"
    try:
        File = open(Filename, "w")
        for x in range(0, 10):
            File.write(FileData[x][0] + "\n")
            File.write(str(FileData[x][1]) + "\n")
        File.close()
    except IOError:
        print("Could not write the file")


# ---- main program ----
if __name__ == "__main__":
    # 1(d)(i)
    ReadHighScores()
    OutputHighScores()  # also the "before" list for 1(e)(iii)
    # 1(e)(i)
    Username = ""
    while len(Username) != 3:
        Username = input("Enter a 3-character player name: ")
    Score = 0
    while Score < 1 or Score > 100000:
        Score = int(input("Enter the score (1 to 100000): "))
    # 1(e)(iii)
    Arrange(Username, Score)
    OutputHighScores()
