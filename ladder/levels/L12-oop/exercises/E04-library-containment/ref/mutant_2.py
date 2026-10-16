# M2: intentional fault from spec.md.
class Book:
    def __init__(self, GivenTitle: str) -> None:
        self.__Title = GivenTitle  # STRING
        self.__OnLoan = False  # BOOLEAN

    def GetTitle(self) -> str:
        return self.__Title

    def GetOnLoan(self) -> bool:
        return self.__OnLoan

    def LendOut(self) -> bool:
        if self.__OnLoan:
            return False
        self.__OnLoan = True
        return True

    def ReturnBook(self) -> None:
        self.__OnLoan = False


class Library:
    def __init__(self) -> None:
        self.__Books = []  # Incorrectly starts with no allocated Book slots
        self.__NumberBooks = 0  # INTEGER

    def AddBook(self, NewBook: Book) -> bool:
        if self.__NumberBooks == 5:
            return False
        self.__Books.append(NewBook)
        self.__NumberBooks = self.__NumberBooks + 1
        return True

    def FindBook(self, Title: str) -> int:
        for Index in range(self.__NumberBooks):
            if self.__Books[Index].GetTitle() == Title:
                return Index
        return -1

    def LendBook(self, Title: str) -> bool:
        Index = self.FindBook(Title)
        if Index == -1:
            return False
        return self.__Books[Index].LendOut()

    def CountOnLoan(self) -> int:
        Count = 0
        for Index in range(self.__NumberBooks):
            if self.__Books[Index].GetOnLoan():
                Count = Count + 1
        return Count
