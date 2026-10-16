# M4: intentional fault from spec.md.
def InsertOne(TheArray: list[int], Index: int) -> None:
    ItemToInsert = TheArray[Index]
    Position = Index - 1
    while Position >= 0 and TheArray[Position] > ItemToInsert:
        TheArray[Position + 1] = TheArray[Position]
        Position = Position - 1
    TheArray[Position + 1] = ItemToInsert


def InsertionSort(TheArray: list[int]) -> None:
    TheArray.sort()
