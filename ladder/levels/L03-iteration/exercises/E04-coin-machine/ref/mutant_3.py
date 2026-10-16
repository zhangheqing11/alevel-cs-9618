PRICE=60
def coin_machine():
 p=0
 while p<PRICE:
  c=int(input()); p+=c; print(f"Due: {PRICE-p}")
 print(f"Change: {p-PRICE}")
