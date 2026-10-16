# M2: intentional fault described in spec.md.
def times_grid() -> None:
    n = int(input("N: "))
    total = 0
    for row in range(1, n + 1):
        total = 0
        line = ""
        for column in range(1, n + 1):
            product = row * column
            line = line + str(product) + " "
            total = total + product
        print(line)
    print(f"Total: {total}")


if __name__ == "__main__":
    times_grid()
