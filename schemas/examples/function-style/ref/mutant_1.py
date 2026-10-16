def linear_search(items: list[int], target: int) -> int:
    # Off-by-one: never checks the last element
    for index in range(len(items) - 1):
        if items[index] == target:
            return index
    return -1
