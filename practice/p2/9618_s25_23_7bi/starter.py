from datetime import date
# Provided Cambridge date-function and customer-lookup adapters.
def TODAY():
    return date.today()

def FindCustomer(CustomerID):
    return CustomerID+',132,05032025'

def MondayCheck(CustomerID):
    """Implement the QP algorithm; preserve this public interface."""
    raise NotImplementedError
