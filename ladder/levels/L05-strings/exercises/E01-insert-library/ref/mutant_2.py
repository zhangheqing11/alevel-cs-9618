# M2: intentional fault from spec.md.
def left(s: str, x: int) -> str:
    return s[:x]


def right(s: str, x: int) -> str:
    return s[-x:]


def mid(s: str, x: int, y: int) -> str:
    return s[x - 1:x - 1 + y]


def length(s: str) -> int:
    return len(s)
