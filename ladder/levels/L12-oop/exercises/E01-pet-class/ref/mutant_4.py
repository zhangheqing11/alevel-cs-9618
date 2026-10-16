# M4: intentional fault from spec.md.
class Pet:
    def __init__(self, GivenName: str, GivenAge: int) -> None:
        self.__Name = GivenName  # STRING
        self.__Age = GivenAge  # INTEGER

    def GetName(self) -> str:
        return self.__Name

    def GetAge(self) -> int:
        return self.__Age

    def SetAge(self, NewAge: int) -> bool:
        if 0 <= NewAge <= 50:
            self.__Age = NewAge
            return True
        return False

    def Birthday(self) -> None:
        Age = self.__Age + 1
