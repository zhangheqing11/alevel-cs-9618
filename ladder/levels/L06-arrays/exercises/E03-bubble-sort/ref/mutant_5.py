# M5: intentional fault from spec.md.
def sort_by_mark(names: list[str], marks: list[int]) -> None:
    pairs = sorted(zip(names, marks), key=lambda pair: pair[1], reverse=True)
    names = [pair[0] for pair in pairs]
    marks = [pair[1] for pair in pairs]
