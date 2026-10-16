# M4: intentional fault from spec.md.
def BinarySearch(SearchArray: list[int], SearchItem: int) -> int:
    for Index in range(len(SearchArray)):
        if SearchArray[Index] == SearchItem:
            return Index
    return -1

def RecursiveBinarySearch(SearchArray: list[int], SearchItem: int, Low: int, High: int) -> int:
    if Low > High:
        return -1
    Mid = (Low + High) // 2
    Value = SearchArray[Mid]
    if Value == SearchItem:
        return Mid
    if SearchItem < Value:
        return RecursiveBinarySearch(SearchArray, SearchItem, Low, Mid - 1)
    return RecursiveBinarySearch(SearchArray, SearchItem, Mid + 1, High)
