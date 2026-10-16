def rogue_average():
 n=int(input()); c=t=0
 while n!=-1:
  c+=1; t+=n; n=int(input())
 print(f"Average: {t/c:.1f}")
