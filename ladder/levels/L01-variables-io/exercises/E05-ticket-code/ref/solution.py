def ticket_code() -> None:
    name = input("Name: ")
    row = int(input("Row: "))
    seat = int(input("Seat: "))
    code = name + "-" + str(row * 100 + seat)
    print(f"Your code is {code}")
    print(f"Row {row}, seat {seat}")


if __name__ == "__main__":
    ticket_code()
