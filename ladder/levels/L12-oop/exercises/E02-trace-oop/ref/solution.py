PREDICTED = ["4 5", "9", "6 9"]


class Counter:
    def __init__(self, GivenStep: int) -> None:
        self.__Count = 0  # INTEGER
        self.__StepSize = GivenStep  # INTEGER

    def Increment(self) -> None:
        self.__Count = self.__Count + self.__StepSize

    def GetCount(self) -> int:
        return self.__Count


class LimitedCounter(Counter):
    def __init__(self, GivenStep: int, GivenLimit: int) -> None:
        super().__init__(GivenStep)
        self.__Limit = GivenLimit  # INTEGER

    def Increment(self) -> None:
        if self.GetCount() < self.__Limit:
            super().Increment()


def RunTrace() -> None:
    A = Counter(2)
    B = Counter(5)
    C = LimitedCounter(3, 7)
    A.Increment()
    A.Increment()
    B.Increment()
    print(A.GetCount(), B.GetCount())
    for Index in range(1, 5):
        C.Increment()
    print(C.GetCount())
    Counters = [A, C]  # Counter, 2 elements
    for CounterObject in Counters:
        CounterObject.Increment()
    print(Counters[0].GetCount(), Counters[1].GetCount())


if __name__ == "__main__":
    RunTrace()
