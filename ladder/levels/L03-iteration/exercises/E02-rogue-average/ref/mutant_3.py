# M3: intentional fault described in spec.md.
def rogue_average() -> None:
    count = 0
    total = 0
    number = int(input("Enter an integer (-1 to stop): "))
    while number != -1:
        count = count + 1
        total = total + number
        number = int(input("Enter an integer (-1 to stop): "))
    print(f"Count: {count}")
    print(f"Total: {total}")
    print(f"Average: {total / count:.1f}")


if __name__ == "__main__":
    rogue_average()
