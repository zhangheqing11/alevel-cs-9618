# 9618_s25_23:7(b)(i) MP6: date-functions
from datetime import date
# Provided Cambridge date-function and customer-lookup adapters.
def TODAY():
    return date.today()

def FindCustomer(CustomerID):
    return CustomerID+',132,05032025'

def MondayCheck(CustomerID):
    Line=FindCustomer(CustomerID)
    LoyaltyPointsString=Line[7:-9]
    LoyaltyPoints=int(LoyaltyPointsString)
    if TODAY().weekday()==1:
        LoyaltyPoints+=10
    return LoyaltyPoints
