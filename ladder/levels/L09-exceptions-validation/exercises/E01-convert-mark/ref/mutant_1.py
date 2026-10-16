# M1: intentional fault from spec.md.
def ConvertMark(MarkString: str) -> int:
    Mark = int(MarkString)
    if 0 <= Mark <= 100:
        return Mark
    return -1
