class Book:
    def __init__(self, GivenTitle: str) -> None:
        raise NotImplementedError   # self.__Title (STRING), self.__OnLoan (BOOLEAN)

    def GetTitle(self) -> str:
        raise NotImplementedError

    def GetOnLoan(self) -> bool:
        raise NotImplementedError

    def LendOut(self) -> bool:
        raise NotImplementedError

    def ReturnBook(self) -> None:
        raise NotImplementedError


class Library:
    def __init__(self) -> None:
        raise NotImplementedError   # self.__Books (Book, 5 elements), self.__NumberBooks (INTEGER)

    def AddBook(self, NewBook: Book) -> bool:
        raise NotImplementedError

    def FindBook(self, Title: str) -> int:
        raise NotImplementedError

    def LendBook(self, Title: str) -> bool:
        raise NotImplementedError

    def CountOnLoan(self) -> int:
        raise NotImplementedError
