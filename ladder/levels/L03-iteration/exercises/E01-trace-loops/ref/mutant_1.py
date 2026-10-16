# M1: intentional fault described in spec.md.
PREDICTED: list[str] = ["A: 12", "B: 5", "C: 10", "D: 5", "D: 3", "D: 1", "F: done"]


def run_trace() -> None:
    total = 0
    for count in range(1, 10, 3):
        total = total + count
    print(f"A: {total}")
    n = 50
    while n > 9:
        n = n - 9
    print(f"B: {n}")
    n = 5
    while True:
        n = n * 2
        if n > 3:
            break
    print(f"C: {n}")
    for count in range(5, 0, -2):
        print(f"D: {count}")
    for count in range(3, 0):
        print(f"E: {count}")
    print("F: done")


if __name__ == "__main__":
    run_trace()
