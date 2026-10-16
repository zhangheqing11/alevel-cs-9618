# M1: intentional fault from spec.md.
PREDICTED = ["Down 3", "Up 3", "Down 2", "Up 2", "Down 1", "Up 1", "Go", "32", "1"]


def Countdown(N: int) -> None:
    if N == 0:
        print("Go")
    else:
        print(f"Down {N}")
        print(f"Up {N}")
        Countdown(N - 1)


def Power(Base: int, Exponent: int) -> int:
    if Exponent == 0:
        return 1
    return Base * Power(Base, Exponent - 1)


def RunTrace() -> None:
    Countdown(3)
    print(Power(2, 5))
    print(Power(7, 0))


if __name__ == "__main__":
    RunTrace()
