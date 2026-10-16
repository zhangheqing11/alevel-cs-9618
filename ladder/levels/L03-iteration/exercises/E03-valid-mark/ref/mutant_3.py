# M3: intentional fault described in spec.md.
def get_mark() -> int:
    while True:
        mark = int(input("Mark (0-100): "))
        print("Invalid: must be 0 to 100")
        if 0 <= mark <= 100:
            return mark
