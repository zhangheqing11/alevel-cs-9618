# M2: intentional fault from spec.md.
def Factorial(N: int) -> int:
    if N == 0:
        return 1
    return N * Factorial(N - 1)


def SumDigits(N: int) -> int:
    Total = 0
    while N > 0:
        Total = Total + N % 10
        N = N // 10
    return Total


def Reverse(Text: str) -> str:
    if Text == "":
        return ""
    return Reverse(Text[1:]) + Text[0]
