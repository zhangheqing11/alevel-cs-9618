# MUTANT 9618_s24_42:1(c)(i) MP3 (assign-value): a correct answer is not replaced with a null value,
# so entering it twice counts twice and it is still listed as missed.
# Question1_J24 -- reference solution (close to the MS Python example, slips fixed)

WordArray = [""] * 100  # global array of STRING: [0] main word, [1..NumberWords] answers
NumberWords = 0  # global INTEGER: number of answers (main word not counted)


# ---- 1(a) and 1(d)(i) ----
def ReadWords(FileName):
    global NumberWords
    try:
        File = open(FileName, "r")
        WordArray[0] = File.readline().strip()
        NumberWords = 0
        Line = File.readline()
        while Line != "":
            NumberWords = NumberWords + 1
            WordArray[NumberWords] = Line.strip()
            Line = File.readline()
        File.close()
    except IOError:
        print("Cannot read file")
    Play()  # 1(d)(i)


# ---- 1(c)(i) and 1(c)(ii) ----
def Play():
    print("The word is:", WordArray[0])
    print("There are", NumberWords, "words that can be made with 3 or more letters")
    QuantityFound = 0
    Answer = input("Enter your word or no to stop: ").lower()
    while Answer != "no":
        Found = False
        for x in range(1, NumberWords + 1):
            if Answer == WordArray[x]:
                QuantityFound = QuantityFound + 1
                Found = True
        if Found:
            print("Correct, you have found", QuantityFound, "words")
        else:
            print("Sorry that was incorrect")
        Answer = input("Enter your word or no to stop: ").lower()
    # 1(c)(ii)
    if NumberWords > 0:
        Correct = QuantityFound / NumberWords * 100
        print("You found", Correct, "%")
    print("The words you missed are")
    for x in range(1, NumberWords + 1):
        if WordArray[x] != "":
            print(WordArray[x])


# ---- main program ----
if __name__ == "__main__":
    # 1(b)
    Choice = input("Easy, medium or hard? ").lower()
    if Choice == "easy":
        FileName = "Easy.txt"
    elif Choice == "medium":
        FileName = "Medium.txt"
    else:
        FileName = "Hard.txt"
    ReadWords(FileName)
