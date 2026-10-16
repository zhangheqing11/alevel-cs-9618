class Pet:
    def __init__(self, GivenName: str, GivenAge: int) -> None:
        raise NotImplementedError   # self.__Name (STRING), self.__Age (INTEGER)

    def GetName(self) -> str:
        raise NotImplementedError

    def GetAge(self) -> int:
        raise NotImplementedError

    def SetAge(self, NewAge: int) -> bool:
        raise NotImplementedError

    def Birthday(self) -> None:
        raise NotImplementedError
