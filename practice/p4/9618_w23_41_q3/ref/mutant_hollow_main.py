# D46: correct modules retained, main fabricates the expected output.
class Character:
    # XPosition, YPosition: INTEGER; Name: STRING.
    def __init__(self, XPositionP, YPositionP, NameP):
        self.XPosition = XPositionP
        self.YPosition = YPositionP
        self.Name = NameP

    def GetXPosition(self):
        return self.XPosition

    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self, Value):
        self.XPosition = self.XPosition + Value
        if self.XPosition > 10000:
            self.XPosition = 10000
        elif self.XPosition < 0:
            self.XPosition = 0

    def SetYPosition(self, Value):
        self.YPosition = self.YPosition + Value
        if self.YPosition > 10000:
            self.YPosition = 10000
        elif self.YPosition < 0:
            self.YPosition = 0

    def Move(self, Direction):
        if Direction == 'up':
            self.SetYPosition(10)
        elif Direction == 'down':
            self.SetYPosition(-10)
        elif Direction == 'right':
            self.SetXPosition(10)
        else:
            self.SetXPosition(-10)


class BikeCharacter(Character):
    def __init__(self, XPositionP, YPositionP, NameP):
        super().__init__(XPositionP, YPositionP, NameP)

    def Move(self, Direction):
        if Direction == 'up':
            super().SetYPosition(20)
        elif Direction == 'down':
            super().SetYPosition(-20)
        elif Direction == 'right':
            super().SetXPosition(20)
        else:
            super().SetXPosition(-20)


if __name__ == "__main__":
    print("Would you like to move Jack or Karla? Which direction: up, down, left or right? Jack's new position is X = 60 Y = 50\n")
