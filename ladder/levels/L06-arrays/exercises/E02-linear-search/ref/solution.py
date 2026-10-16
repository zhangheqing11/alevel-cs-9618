def look_up_mark(names: list[str], marks: list[int], search_name: str) -> int:
    for index in range(len(names)):
        if names[index].upper() == search_name.upper():
            return marks[index]
    return -1
