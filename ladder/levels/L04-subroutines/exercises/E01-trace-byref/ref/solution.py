PREDICTED = ["In AddOne: 4", "A: 3", "A: 8 B: 3", "A: 18"]


def add_one(n: int) -> None:
    n = n + 1
    print(f"In AddOne: {n}")


def swap(x: int, y: int) -> tuple[int, int]:
    return y, x


def twice(n: int) -> int:
    return n * 2


def run_trace() -> None:
    a = 3
    b = 8
    add_one(a)
    print(f"A: {a}")
    a, b = swap(a, b)
    print(f"A: {a} B: {b}")
    a = twice(a) + twice(1)
    print(f"A: {a}")


if __name__ == "__main__":
    run_trace()
