def count_digits(n):
 c=1
 while n>0:c+=1;n//=10
 return c
def digit_sum(n):
 t=0
 while n>0:t+=n%10;n//=10
 return t
