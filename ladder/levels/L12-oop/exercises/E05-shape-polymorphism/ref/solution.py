import math


class Shape:
    def __init__(self, GivenName: str) -> None:
        self.__Name = GivenName  # STRING

    def GetName(self) -> str:
        return self.__Name

    def GetArea(self) -> float:
        return 0.0

    def Describe(self) -> str:
        return f"{self.GetName()}: {self.GetArea():.2f}"


class Rectangle(Shape):
    def __init__(self, GivenWidth: float, GivenHeight: float) -> None:
        super().__init__("Rectangle")
        self.__Width = GivenWidth  # REAL
        self.__Height = GivenHeight  # REAL

    def GetArea(self) -> float:
        return self.__Width * self.__Height


class Circle(Shape):
    def __init__(self, GivenRadius: float) -> None:
        super().__init__("Circle")
        self.__Radius = GivenRadius  # REAL

    def GetArea(self) -> float:
        return math.pi * self.__Radius * self.__Radius


def TotalArea(Shapes: list[Shape]) -> float:
    Total = 0.0
    for Item in Shapes:
        Total = Total + Item.GetArea()
    return Total
