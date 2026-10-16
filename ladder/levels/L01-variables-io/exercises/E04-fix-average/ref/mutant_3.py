# M3: intentional fault described in spec.md.
def mark_summary() -> None:
    mark1 = int(input("Mark 1: "))
    mark2 = int(input("Mark 2: "))
    mark3 = int(input("Mark 3: "))
    total = mark1 + mark2 + mark3
    average = total / 3
    print(f"Total: {total}")
    print(f"Average: {round(average)}")


if __name__ == "__main__":
    mark_summary()
