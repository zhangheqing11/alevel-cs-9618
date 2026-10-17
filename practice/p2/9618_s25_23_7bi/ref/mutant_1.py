# 9618_s25_23:7(b)(i) MP4: field-extract
from datetime import date
# Provided Cambridge date-function and customer-lookup adapters.
def TODAY():
    return date.today()

def FindCustomer(CustomerID):
    return CustomerID+',132,05032025'

def MondayCheck(CustomerID):
    Line=FindCustomer(CustomerID)
    LoyaltyPointsString=Line[7:10]
    LoyaltyPoints=int(LoyaltyPointsString)
    if TODAY().weekday()==0:
        LoyaltyPoints+=10
    return LoyaltyPoints
