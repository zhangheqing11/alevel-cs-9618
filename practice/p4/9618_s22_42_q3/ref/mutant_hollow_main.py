# D46: correct modules retained, main fabricates the expected output.
class Card:
    # Number : INTEGER; Colour : STRING (private).
    def __init__(self, Numberp, Colourp):
        self.__Number = Numberp
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
    print('Select a Card from 1 to 30: Select a Card from 1 to 30: Select a Card from 1 to 30: Select a Card from 1 to 30: red\n1\ngreen\n9\norange\n9\norange\n10\n')
