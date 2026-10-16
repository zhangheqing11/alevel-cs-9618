# M1: intentional fault described in spec.md.
def split_seconds() -> None:
    total = int(input("Enter seconds: "))
    hours = total / 3600
    minutes = (total % 3600) / 60
    seconds = total % 60
    print(f"{hours} h {minutes} min {seconds} s")


if __name__ == "__main__":
    split_seconds()
