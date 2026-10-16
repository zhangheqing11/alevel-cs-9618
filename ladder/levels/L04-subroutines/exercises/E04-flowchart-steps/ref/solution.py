def count_steps() -> None:
    number = int(input("Positive integer: "))
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        steps = steps + 1
    print(f"Steps: {steps}")


if __name__ == "__main__":
    count_steps()
