# 9618_s25_23:7(a)(i) MP6: date-functions
from datetime import date
# Provided Cambridge date-function adapter, replaced by tests for determinism.
def TODAY():
    return date.today()

def UpdateVisit(LoyaltyPoints,LastVisitDate):
    CurrentDate=TODAY()
    if CurrentDate.month==LastVisitDate[0].month:
        LoyaltyPoints[0]+=4
    else:
        LoyaltyPoints[0]+=1
    LastVisitDate=CurrentDate
