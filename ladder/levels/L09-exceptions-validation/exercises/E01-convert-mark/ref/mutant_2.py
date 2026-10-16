# M2: intentional fault from spec.md.
def ConvertMark(MarkString: str) -> int:
    if not MarkString.isdigit():
        return -1
    Mark = int(MarkString)
    if 0 <= Mark <= 100:
        return Mark
    return -1
