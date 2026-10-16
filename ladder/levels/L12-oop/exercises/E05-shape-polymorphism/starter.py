import math


class Shape:
    def __init__(self, GivenName: str) -> None:
        raise NotImplementedError   # self.__Name (STRING)

    def GetName(self) -> str:
        raise NotImplementedError

    def GetArea(self) -> float:
        raise NotImplementedError

    def Describe(self) -> str:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, GivenWidth: float, GivenHeight: float) -> None:
        raise NotImplementedError   # parent constructor; self.__Width, self.__Height (REAL)

    def GetArea(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, GivenRadius: float) -> None:
        raise NotImplementedError   # parent constructor; self.__Radius (REAL)

    def GetArea(self) -> float:
        raise NotImplementedError


def TotalArea(Shapes: list[Shape]) -> float:
    """Return the sum of GetArea() for every shape in the list."""
    raise NotImplementedError
