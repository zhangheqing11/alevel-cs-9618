# M3: intentional fault from spec.md.
def BinarySearch(SearchArray: list[int], SearchItem: int) -> int:
    Low = 0
    High = len(SearchArray) - 1
    while Low <= High:
        Mid = (Low + High) // 2
        Value = SearchArray[Mid]
        if Value == SearchItem:
            return Mid
        if SearchItem < Value:
            High = Mid - 1
        else:
            Low = Mid + 1
    return -1


def RecursiveBinarySearch(SearchArray: list[int], SearchItem: int, Low: int, High: int) -> int:
    if Low > High:
        return -1
    Mid = (Low + High) // 2
    Value = SearchArray[Mid]
    if Value == SearchItem:
        return Mid
    if SearchItem < Value:
        RecursiveBinarySearch(SearchArray, SearchItem, Low, Mid - 1)
    RecursiveBinarySearch(SearchArray, SearchItem, Mid + 1, High)
