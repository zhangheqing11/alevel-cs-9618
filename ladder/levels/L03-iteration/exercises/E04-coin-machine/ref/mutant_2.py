PRICE=60
def coin_machine():
 p=0
 while p<PRICE:
  p+=int(input())
 print(f"Change: {p-PRICE}")
