# M1: intentional fault from spec.md.
def left(s: str, x: int) -> str:
    return s[:x]


def right(s: str, x: int) -> str:
    if x == 0:
        return ""
    return s[-x:]


def mid(s: str, x: int, y: int) -> str:
    return s[x:x + y]


def length(s: str) -> int:
    return len(s)
