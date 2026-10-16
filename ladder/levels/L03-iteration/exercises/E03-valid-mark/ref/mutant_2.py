# M2: intentional fault described in spec.md.
def get_mark() -> int:
    while True:
        text = input("Mark (0-100): ")
        mark = int(text)
        if 0 <= mark <= 100:
            return text
        print("Invalid: must be 0 to 100")
