PREDICTED=[1.5,3.,3.2,5.2,10.4,12.4]
def postage(w,e):
 c=1.5 if w<=100 else 3.0 if w<=500 else 3+(w-500)//250+1*1.2
 return c*2 if e else c
