# M1: intentional fault from spec.md.
class Pet:
    def __init__(self, GivenName: str, GivenAge: int) -> None:
        self.Name = GivenName  # STRING
        self.Age = GivenAge  # INTEGER

    def GetName(self) -> str:
        return self.Name

    def GetAge(self) -> int:
        return self.Age

    def SetAge(self, NewAge: int) -> bool:
        if 0 <= NewAge <= 50:
            self.Age = NewAge
            return True
        return False

    def Birthday(self) -> None:
        self.Age = self.Age + 1
