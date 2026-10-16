def InsertOne(TheArray: list[int], Index: int) -> None:
    """Insert TheArray[Index] into the sorted part TheArray[0..Index-1], in place."""
    raise NotImplementedError


def InsertionSort(TheArray: list[int]) -> None:
    """Sort TheArray in place by calling InsertOne() for Index = 1 .. len - 1."""
    raise NotImplementedError
