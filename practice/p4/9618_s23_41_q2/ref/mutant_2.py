# 9618_s23_41:2(a)(iv) MP3: assign-value.
class Vehicle:
    # ID : STRING; MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition : INTEGER.
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__IncreaseAmount

    def OutputCurrentPosition(self):
        print("Current position =", self.__HorizontalPosition)
        print("Current speed =", self.__CurrentSpeed)


class Helicopter(Vehicle):
    # VerticalPosition, VerticalChange, MaxHeight : INTEGER (private).
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0
        self.__VerticalChange = VertChangeP
        self.__MaxHeight = MaxHeightP

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()

    def OutputCurrentPosition(self):
        super().OutputCurrentPosition()
        print("Current vertical position =", self.__VerticalPosition)


if __name__ == "__main__":
    Car = Vehicle("Tiger",100,20)
    Heli1 = Helicopter("Lion",350,40,3,100)
    Car.IncreaseSpeed()
    Car.IncreaseSpeed()
    Car.OutputCurrentPosition()
    Heli1.IncreaseSpeed()
    Heli1.IncreaseSpeed()
    Heli1.OutputCurrentPosition()
