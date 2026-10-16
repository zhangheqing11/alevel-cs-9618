def times_grid():
 n=int(input()); t=0
 for r in range(1,n+1): print("".join(str(r*c) for c in range(1,n+1)))
 print(f"Total: {t}")
