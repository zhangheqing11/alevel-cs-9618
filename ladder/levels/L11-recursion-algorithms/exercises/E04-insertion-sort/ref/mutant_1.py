# M1: intentional fault from spec.md.
def InsertOne(TheArray: list[int], Index: int) -> None:
    if Index > 0 and TheArray[Index - 1] > TheArray[Index]:
        TheArray[Index - 1], TheArray[Index] = TheArray[Index], TheArray[Index - 1]

def InsertionSort(TheArray: list[int]) -> None:
    for Index in range(1, len(TheArray)):
        InsertOne(TheArray, Index)
