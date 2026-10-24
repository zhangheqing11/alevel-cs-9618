# 9618_s22_42:3(a) MP5: constructor.
class Card:
    # Number : INTEGER; Colour : STRING (private).
    def __init__(self, Numberp, Colourp):
        self.__Number = 0
        self.__Colour = Colourp

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


NumbersChosen = [False] * 30  # 30 BOOLEAN selection flags.


def ChooseCard():
    while True:
        CardSelected = int(input("Select a Card from 1 to 30: "))
        if CardSelected < 1 or CardSelected > 30:
            print("Number must be between 1 and 30")
        elif NumbersChosen[CardSelected - 1]:
            print("Already taken")
        else:
            NumbersChosen[CardSelected - 1] = True
            return CardSelected - 1


if __name__ == "__main__":
    CardArray = [None] * 30  # 30 Card objects.
    try:
        with open("CardValues.txt", "r") as File:
            for x in range(30):
                NumberRead = int(File.readline())
                ColourRead = File.readline().rstrip("\r\n")
                CardArray[x] = Card(NumberRead, ColourRead)
    except IOError:
        print("Could not find file")
    Player1 = [None] * 4  # 4 Card objects.
    for x in range(4):
        ReturnNumber = ChooseCard()
        Player1[x] = CardArray[ReturnNumber]
    for x in range(4):
        print(Player1[x].GetColour())
        print(Player1[x].GetNumber())
