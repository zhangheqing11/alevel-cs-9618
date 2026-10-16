# M3: intentional fault from spec.md.
def look_up_mark(names: list[str], marks: list[int], search_name: str) -> int:
    result = -1
    for index in range(len(names)):
        if names[index].upper() == search_name.upper():
            result = marks[index]
    return result
