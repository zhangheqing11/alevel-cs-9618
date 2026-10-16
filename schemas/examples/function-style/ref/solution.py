def linear_search(items: list[int], target: int) -> int:
    """Return the index of the first occurrence of target in items, or -1."""
    for index in range(len(items)):
        if items[index] == target:
            return index
    return -1
