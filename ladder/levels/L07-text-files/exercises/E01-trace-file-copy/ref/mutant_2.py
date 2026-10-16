# M2: intentional fault from spec.md.
PREDICTED_FILE = ["1: APPLE", "2: BANANA", "3: CHERRY", "4: DATE"]
PREDICTED_OUTPUT = ["Lines written: 4", "Blank lines: 2"]


def run_trace() -> None:
    count = 0
    blank = 0
    with open("words.txt", encoding="utf-8") as source, open("out.txt", "a", encoding="utf-8") as target:
        for raw_line in source:
            line = raw_line.rstrip("\n")
            if line == "":
                blank = blank + 1
            else:
                count = count + 1
                target.write(str(count) + ": " + line.upper() + "\n")
    print(f"Lines written: {count}")
    print(f"Blank lines: {blank}")


if __name__ == "__main__":
    run_trace()
