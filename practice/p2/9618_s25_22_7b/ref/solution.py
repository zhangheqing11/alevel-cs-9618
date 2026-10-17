# Provided global INTEGER ARRAY[1:1000,1:2]; Python indices = QP - 1.
Loyalty=[[99999,0] for _ in range(1000)]

def PointsReport():
    Count=0
    Sum=0
    for Index in range(1000):
        if Loyalty[Index][0]==99999:
            break
        if Loyalty[Index][1]>=11:
            print(Loyalty[Index][0])
        Count+=1
        Sum+=Loyalty[Index][1]
    print('The average points of all the customers is '+str(Sum/Count))
