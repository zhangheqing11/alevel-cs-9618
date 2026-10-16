# M1: intentional fault from spec.md.
def tally(rolls: list[int]) -> list[int]:
    counts = [0] * 6  # ARRAY[1:6] OF INTEGER
    for roll in rolls:
        counts[roll] = counts[roll] + 1
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
