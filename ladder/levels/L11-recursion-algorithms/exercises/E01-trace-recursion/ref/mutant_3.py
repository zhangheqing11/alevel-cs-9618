# M3: intentional fault from spec.md.
PREDICTED = ["Down 3", "Down 2", "Down 1", "Go", "Up 1", "Up 2", "Up 3", "32", "1"]


def Countdown(N: int) -> None:
    if N == 0:
        print("Go")
    else:
        print(f"Down {N}")
        Countdown(N - 1)
        print(f"Up {N}")


def Power(Base: int, Exponent: int) -> int:
    Result = 1
    for _ in range(Exponent):
        Result = Result * Base
    return Result


def RunTrace() -> None:
    Countdown(3)
    print(Power(2, 5))
    print(Power(7, 0))


if __name__ == "__main__":
    RunTrace()
