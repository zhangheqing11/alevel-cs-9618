# M2: intentional fault described in spec.md.
PRICE = 60


def coin_machine() -> None:
    paid = 0
    while True:
        coin = int(input("Insert coin: "))
        paid = paid + coin
        if paid < PRICE:
            print(f"Due: {PRICE - paid}")
        if paid >= PRICE:
            break
    print(f"Change: {paid - PRICE}")


if __name__ == "__main__":
    coin_machine()
