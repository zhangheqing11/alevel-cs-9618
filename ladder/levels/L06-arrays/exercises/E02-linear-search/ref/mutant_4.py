# M4: intentional fault from spec.md.
def look_up_mark(names: list[str], marks: list[int], search_name: str) -> int:
    for index in range(len(names) - 1):
        if names[index].upper() == search_name.upper():
            return marks[index]
    return -1
