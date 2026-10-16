# M2: intentional fault from spec.md.
def look_up_mark(names: list[str], marks: list[int], search_name: str) -> int:
    for index in range(len(names)):
        if names[index] == search_name:
            return marks[index]
    return -1
