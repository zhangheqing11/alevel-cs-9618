def ConvertMark(MarkString: str) -> int:
    try:
        Mark = int(MarkString)
    except ValueError:
        return -1
    if 0 <= Mark <= 100:
        return Mark
    return -1
