# M2: intentional fault from spec.md.
def to_minutes(hours: int, minutes: int) -> int:
    return hours * 60 + minutes


def split_minutes(total: int) -> tuple[int, int]:
    hours = total // 60
    minutes = total % 60


def add_durations(h1: int, m1: int, h2: int, m2: int) -> None:
    total = to_minutes(h1, m1) + to_minutes(h2, m2)
    hours, minutes = split_minutes(total)
    print(f"Total: {hours} h {minutes} min")
