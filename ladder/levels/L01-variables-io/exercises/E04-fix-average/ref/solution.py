def mark_summary() -> None:
    mark1 = int(input("Mark 1: "))
    mark2 = int(input("Mark 2: "))
    mark3 = int(input("Mark 3: "))
    total = mark1 + mark2 + mark3
    average = total / 3
    print(f"Total: {total}")
    print(f"Average: {average:.1f}")


if __name__ == "__main__":
    mark_summary()
