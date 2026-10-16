# M1: intentional fault described in spec.md.
def rogue_average() -> None:
    count = 0
    total = 0
    number = int(input("Enter an integer (-1 to stop): "))
    while True:
        count = count + 1
        total = total + number
        if number == -1:
            break
        number = int(input("Enter an integer (-1 to stop): "))
    if count == 0:
        print("No data")
    else:
        print(f"Count: {count}")
        print(f"Total: {total}")
        print(f"Average: {total / count:.1f}")


if __name__ == "__main__":
    rogue_average()
