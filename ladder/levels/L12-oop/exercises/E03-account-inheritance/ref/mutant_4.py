# M4: intentional fault from spec.md.
class Account:
    def __init__(self, GivenNumber: str) -> None:
        self.__AccountNumber = GivenNumber  # STRING
        self.__Balance = 0.0  # REAL

    def GetAccountNumber(self) -> str:
        return self.__AccountNumber

    def GetBalance(self) -> float:
        return self.__Balance

    def Deposit(self, Amount: float) -> bool:
        if Amount > 0:
            self.__Balance = self.__Balance + Amount
            return True
        return False

    def Withdraw(self, Amount: float) -> bool:
        if Amount > 0 and Amount <= self.__Balance:
            self.__Balance = self.__Balance - Amount
            return True
        return False


class SavingsAccount(Account):
    def __init__(self, GivenNumber: str, GivenRate: float) -> None:
        self.__Balance = 0.0  # REAL; wrongly redeclared in the child
        self.__InterestRate = GivenRate  # REAL
        self.__WithdrawalsLeft = 2  # INTEGER

    def GetWithdrawalsLeft(self) -> int:
        return self.__WithdrawalsLeft

    def AddInterest(self) -> None:
        self.Deposit(self.GetBalance() * self.__InterestRate)

    def Withdraw(self, Amount: float) -> bool:
        if self.__WithdrawalsLeft == 0:
            return False
        Result = super().Withdraw(Amount)
        if Result:
            self.__WithdrawalsLeft = self.__WithdrawalsLeft - 1
        return Result
