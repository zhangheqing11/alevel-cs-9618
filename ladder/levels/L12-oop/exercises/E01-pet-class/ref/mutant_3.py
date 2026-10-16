# M3: intentional fault from spec.md.
class Pet:
    def __init__(self, GivenName: str, GivenAge: int) -> None:
        self.__Name = GivenName  # STRING
        self.__Age = GivenAge  # INTEGER

    def GetName(self) -> str:
        return self.__Name

    def GetAge(self) -> int:
        return self.__Age

    def SetAge(self, NewAge: int) -> bool:
        self.__Age = NewAge
        return True

    def Birthday(self) -> None:
        self.__Age = self.__Age + 1
