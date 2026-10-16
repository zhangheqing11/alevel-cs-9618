PRICE = 60


def coin_machine() -> None:
    paid = 0
    while True:
        coin = int(input("Insert coin: "))
        if coin == 10 or coin == 20 or coin == 50:
            paid = paid + coin
        else:
            print(f"Rejected: {coin}")
        if paid < PRICE:
            print(f"Due: {PRICE - paid}")
        if paid >= PRICE:
            break
    print(f"Change: {paid - PRICE}")


if __name__ == "__main__":
    coin_machine()
