PREDICTED: list[str] = []  # fill in by hand BEFORE writing the code


class Counter:
    def __init__(self, GivenStep: int) -> None:
        raise NotImplementedError   # self.__Count (INTEGER), self.__StepSize (INTEGER)

    def Increment(self) -> None:
        raise NotImplementedError

    def GetCount(self) -> int:
        raise NotImplementedError


class LimitedCounter(Counter):
    def __init__(self, GivenStep: int, GivenLimit: int) -> None:
        raise NotImplementedError   # call the parent constructor; self.__Limit (INTEGER)

    def Increment(self) -> None:
        raise NotImplementedError


def RunTrace() -> None:
    """Run the main program."""
    raise NotImplementedError


if __name__ == "__main__":
    RunTrace()
