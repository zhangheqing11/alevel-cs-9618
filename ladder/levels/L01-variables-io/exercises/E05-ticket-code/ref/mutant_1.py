# M1: intentional fault described in spec.md.
def ticket_code() -> None:
    name = input("Name: ")
    row = input("Row: ")
    seat = input("Seat: ")
    code = name + "-" + row * 100 + seat
    print(f"Your code is {code}")
    print(f"Row {row}, seat {seat}")


if __name__ == "__main__":
    ticket_code()
