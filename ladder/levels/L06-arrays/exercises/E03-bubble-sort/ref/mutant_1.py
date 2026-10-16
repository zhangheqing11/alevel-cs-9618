# M1: intentional fault from spec.md.
def sort_by_mark(names: list[str], marks: list[int]) -> None:
    boundary = len(marks) - 1
    swapped = True
    while swapped and boundary > 0:
        swapped = False
        for index in range(boundary):
            if marks[index] < marks[index + 1]:
                marks[index], marks[index + 1] = marks[index + 1], marks[index]
                swapped = True
        boundary = boundary - 1
