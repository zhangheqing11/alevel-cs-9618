# M2: intentional fault from spec.md.
def tally(rolls: list[int]) -> list[int]:
    counts = []
    seen = []
    for roll in rolls:
        if roll not in seen:
            seen.append(roll)
            counts.append(rolls.count(roll))
    return counts


def most_frequent(rolls: list[int]) -> int:
    if not rolls:
        return 0
    counts = tally(rolls)
    best = 0
    for index in range(1, 6):
        if counts[index] > counts[best]:
            best = index
    return best + 1
