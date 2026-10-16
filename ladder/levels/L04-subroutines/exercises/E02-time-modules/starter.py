def to_minutes(hours: int, minutes: int) -> int:
    """Return hours * 60 + minutes."""
    raise NotImplementedError


def split_minutes(total: int) -> tuple[int, int]:
    """Return (whole hours, remaining minutes). Replaces the two BYREF parameters."""
    raise NotImplementedError


def add_durations(h1: int, m1: int, h2: int, m2: int) -> None:
    """Use to_minutes() and split_minutes(); print 'Total: <h> h <m> min'."""
    raise NotImplementedError
