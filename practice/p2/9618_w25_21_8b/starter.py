# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:5000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(5000)]

def ReturnBook(ThisStudentID,ThisBookID):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
