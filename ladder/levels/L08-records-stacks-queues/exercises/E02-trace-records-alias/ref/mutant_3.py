# M3: intentional fault from spec.md.
from copy import copy

PREDICTED = ["7 7", "Student1: 10", "Student2: 11", "Student3: 10"]


class PupilRecord:
    """Record type PupilRecord."""

    def __init__(self) -> None:
        self.last_name = ""
        self.year_group = 0


def run_trace() -> None:
    pupil1 = PupilRecord()
    pupil1.last_name = "Johnson"
    pupil1.year_group = 6
    pupil2 = copy(pupil1)
    pupil1.year_group = 7
    print(pupil1.year_group, pupil2.year_group)
    form = [PupilRecord() for _ in range(3)]  # ARRAY[1:3] OF PupilRecord
    for index in range(1, 4):
        form[index - 1].last_name = "Student" + str(index)
        form[index - 1].year_group = 10
    form[1].year_group = form[1].year_group + 1
    for index in range(1, 4):
        print(f"{form[index - 1].last_name}: {form[index - 1].year_group}")


if __name__ == "__main__":
    run_trace()
