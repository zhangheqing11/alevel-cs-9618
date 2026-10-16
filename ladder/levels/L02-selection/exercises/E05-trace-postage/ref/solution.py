PREDICTED=[1.50,3.00,4.20,5.40,10.80,13.20]
def postage(weight:int,express:bool)->float:
    if weight<=100: cost=1.5
    elif weight<=500: cost=3.0
    else: cost=3.0+((weight-500)//250+1)*1.2
    if express: cost*=2
    return cost
