# M1: intentional fault described in spec.md.
PREDICTED: list[str] = ["3", "2", "3.4", "3 7", "ID-42", "34", "Mean is 3.4!"]
PREFIX = "ID-"


def run_trace() -> None:
    total = 17
    count = 5
    mean = total / count
    print(total // count)
    print(total % count)
    print(mean)
    count = count + 2
    total = total - count * 2
    print(total, " ", count)
    code = PREFIX + "42"
    print(code)
    print(int(mean * 10))
    print("Mean is ", mean, "!")


if __name__ == "__main__":
    run_trace()
