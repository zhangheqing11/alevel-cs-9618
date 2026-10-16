# M1: intentional fault described in spec.md.
SERVICE_RATE = 0.10


def split_bill() -> None:
    bill = float(input("Bill: "))
    people = int(input("People: "))
    total = bill * (1 + SERVICE_RATE)
    each = total // people
    print(f"Total: {total:.2f}")
    print(f"Each: {each:.2f}")


if __name__ == "__main__":
    split_bill()
