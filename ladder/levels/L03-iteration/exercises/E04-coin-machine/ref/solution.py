PRICE=60
def coin_machine():
    paid=0
    while paid<PRICE:
        coin=int(input("Coin: "))
        if coin in (10,20,50): paid+=coin
        else: print(f"Rejected: {coin}")
        if paid<PRICE: print(f"Due: {PRICE-paid}")
    print(f"Change: {paid-PRICE}")
if __name__=="__main__": coin_machine()
