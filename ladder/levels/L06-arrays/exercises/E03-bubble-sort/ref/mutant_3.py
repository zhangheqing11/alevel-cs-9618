# M3: intentional fault from spec.md.
def sort_by_mark(names: list[str], marks: list[int]) -> None:
    for pass_number in range(len(marks) - 1):
        for index in range(len(marks) - 1 - pass_number):
            if marks[index] <= marks[index + 1]:
                marks[index], marks[index + 1] = marks[index + 1], marks[index]
                names[index], names[index + 1] = names[index + 1], names[index]
