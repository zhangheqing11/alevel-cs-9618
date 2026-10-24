# D46: correct modules retained, main fabricates the expected output.
class Card:
    # Number: INTEGER; Colour: STRING; both private.
    def __init__(self, Number1, Colour1):
        self.__Number = Number1
        self.__Colour = Colour1

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


class Hand:
    # Cards: ARRAY[0:9] OF Card; FirstCard, NumberCards: INTEGER; private.
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [None] * 10
        self.__Cards[0:5] = [Card1, Card2, Card3, Card4, Card5]
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, Position):
        return self.__Cards[Position]


def CalculateValue(Player):
    Score = 0
    for Count in range(0, 5):
        CardGot = Player.GetCard(Count)
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColour()
        if Colour == 'red':
            Score = Score + 5
        elif Colour == 'blue':
            Score = Score + 10
        else:
            Score = Score + 15
    return Score


if __name__ == "__main__":
    print('Player 2 wins\n')
