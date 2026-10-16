# M3: intentional fault from spec.md.
def InsertOne(TheArray: list[int], Index: int) -> None:
    ItemToInsert = TheArray[Index]
    Position = Index - 1
    while Position >= 0 and TheArray[Position] > ItemToInsert:
        TheArray[Position + 1] = TheArray[Position]
        Position = Position - 1
    TheArray[Position + 1] = ItemToInsert


def InsertionSort(TheArray: list[int]) -> None:
    for Index in range(1, len(TheArray) - 1):
        InsertOne(TheArray, Index)
