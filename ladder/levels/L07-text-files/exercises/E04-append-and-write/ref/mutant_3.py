# M3: intentional fault from spec.md.
def append_entry(file_name: str, entry: str) -> None:
    with open(file_name, "a", encoding="utf-8") as target:
        target.write(entry + "\n")


def write_report(file_name: str, names: list[str], marks: list[int]) -> None:
    with open(file_name, "a", encoding="utf-8") as target:
        target.write("Name,Mark\n")
        for name, mark in zip(names, marks):
            target.write(name + "," + str(mark) + "\n")
