# M3: intentional fault from spec.md.
def filter_marks(in_name: str, out_name: str, pass_mark: int) -> int:
    excluded = 0
    with open(in_name, encoding="utf-8") as source, open(out_name, "w", encoding="utf-8") as target:
        for raw_line in source:
            line = raw_line.rstrip("\n")
            if line == "":
                excluded = excluded + 1
                continue
            name, mark = line.split(",")
            if int(mark) >= pass_mark:
                target.write(line + "\n")
            else:
                excluded = excluded + 1
    return excluded
