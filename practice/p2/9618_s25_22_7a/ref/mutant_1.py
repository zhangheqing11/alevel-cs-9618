# 9618_s25_22:7(a) MP4: linear-search
# Provided global INTEGER ARRAY[1:1000,1:2]; Python indices = QP - 1.
Loyalty=[[99999,0] for _ in range(1000)]

def FindCustomer(CustomerID):
    if CustomerID<10001 or CustomerID>11000:
        return -1
    for Index in range(1000):
        if Loyalty[Index][1]==CustomerID:
            return Loyalty[Index][1]
        if Loyalty[Index][0]==99999:
            return -1
    return -1
