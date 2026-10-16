# M3: intentional fault from spec.md.
def to_minutes(hours: int, minutes: int) -> int:
    return hours * 60 + minutes


def split_minutes(total: int) -> tuple[int, int]:
    return total // 60, total % 60


def add_durations(h1: int, m1: int, h2: int, m2: int) -> None:
    hours = h1 + h2
    minutes = m1 + m2
    print(f"Total: {hours} h {minutes} min")
