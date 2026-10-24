# 9618_w22_42:2(c) MP2 assign-value: reverse horizontal change.
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
        self.__XCoordinate = self.__XCoordinate - XChange
        self.__YCoordinate = self.__YCoordinate + YChange


if __name__ == '__main__':
    Characters = [None] * 10  # ARRAY[0:9] OF Character
    try:
        File = open('Characters.txt', 'r')
        for X in range(10):
            Name = File.readline().strip()
            XCoord = int(File.readline().strip())
            YCoord = int(File.readline().strip())
            Characters[X] = Character(Name, XCoord, YCoord)
        File.close()
    except OSError:
        print('File not found')
        raise SystemExit
    Position = -1
    while Position == -1:
        CharacterInput = input('Enter the character to move: ').lower()
        for Count in range(10):
            if Characters[Count].GetName().lower() == CharacterInput:
                Position = Count
    IsValid = False
    while not IsValid:
        Move = input('Enter A, W, S or D: ').upper()
        if Move == 'A':
            Characters[Position].ChangePosition(-1, 0)
            IsValid = True
        elif Move == 'W':
            Characters[Position].ChangePosition(0, 1)
            IsValid = True
        elif Move == 'S':
            Characters[Position].ChangePosition(0, -1)
            IsValid = True
        elif Move == 'D':
            Characters[Position].ChangePosition(1, 0)
            IsValid = True
    print(Characters[Position].GetName(), 'has changed coordinates to X =',
          Characters[Position].GetX(), 'and Y =', Characters[Position].GetY())
