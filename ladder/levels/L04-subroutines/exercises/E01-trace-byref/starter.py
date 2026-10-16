PREDICTED: list[str] = []  # fill in by hand BEFORE writing the functions


def add_one(n: int) -> None:
    """Print 'In AddOne: <n + 1>'. The caller's variable must not change (BYVAL)."""
    raise NotImplementedError


def swap(x: int, y: int) -> tuple[int, int]:
    """Return (y, x): Python's way of getting the effect of BYREF X, Y."""
    raise NotImplementedError


def twice(n: int) -> int:
    """Return n * 2."""
    raise NotImplementedError


def run_trace() -> None:
    """Run the main program: A = 3, B = 8, then the six statements in order."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
