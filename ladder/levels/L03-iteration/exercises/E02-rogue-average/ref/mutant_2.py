def rogue_average():
 n=int(input()); c=t=0
 while n>0:
  c+=1; t+=n; n=int(input())
 print("No data" if c==0 else f"Count: {c}")
