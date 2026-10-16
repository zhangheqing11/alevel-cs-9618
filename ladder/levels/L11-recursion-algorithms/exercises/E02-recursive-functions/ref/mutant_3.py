# M3: intentional fault from spec.md.
def Factorial(N: int) -> int:
    if N == 0:
        return 1
    return N * Factorial(N - 1)


def SumDigits(N: int) -> int:
    if N < 10:
        return N
    return N % 10 + SumDigits(N // 10)


def Reverse(Text: str) -> str:
    if Text == "":
        return ""
    return Text[0] + Reverse(Text[1:])
