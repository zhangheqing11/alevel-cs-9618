class Account:
    def __init__(self, GivenNumber: str) -> None:
        raise NotImplementedError   # self.__AccountNumber (STRING), self.__Balance (REAL)

    def GetAccountNumber(self) -> str:
        raise NotImplementedError

    def GetBalance(self) -> float:
        raise NotImplementedError

    def Deposit(self, Amount: float) -> bool:
        raise NotImplementedError

    def Withdraw(self, Amount: float) -> bool:
        raise NotImplementedError


class SavingsAccount(Account):
    def __init__(self, GivenNumber: str, GivenRate: float) -> None:
        raise NotImplementedError   # parent constructor; self.__InterestRate (REAL), self.__WithdrawalsLeft (INTEGER)

    def GetWithdrawalsLeft(self) -> int:
        raise NotImplementedError

    def AddInterest(self) -> None:
        raise NotImplementedError

    def Withdraw(self, Amount: float) -> bool:
        raise NotImplementedError
