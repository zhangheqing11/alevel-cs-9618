# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:7000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(7000)]

def NewLoan(ThisStudentID,ThisBookID):
    for Index in range(7000):
        if Loan[Index].StudentID=='':
            Loan[Index].StudentID=ThisStudentID
            Loan[Index].BookID=ThisBookID
            Loan[Index].OnLoan=True
            return True
    return False
