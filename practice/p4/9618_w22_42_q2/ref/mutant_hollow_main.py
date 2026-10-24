# D46: correct modules retained, main fabricates the expected output.
class Character:
    # Name: STRING; XCoordinate, YCoordinate: INTEGER; private.
    def __init__(self, Namep, XCoord, YCoord):
        self.__Name = Namep
        self.__XCoordinate = XCoord
        self.__YCoordinate = YCoord

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange


if __name__ == "__main__":
    print('Enter the character to move: Enter the character to move: Enter A, W, S or D: Enter A, W, S or D: Qui has changed coordinates to X = 83 and Y = 9\n')
