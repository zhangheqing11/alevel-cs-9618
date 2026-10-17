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
    LastVisitDate[0]=CurrentDate
