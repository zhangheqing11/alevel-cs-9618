# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:8000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(8000)]

def LoanStatus(ThisStudentID,ThisBookID):
    for Index in range(8000):
        if Loan[Index].StudentID==ThisStudentID and Loan[Index].BookID==ThisBookID:
            if Loan[Index].OnLoan:
                print('Loan has not been returned.')
            else:
                print('Loan has been returned.')
            return
    print('Warning - Loan not found.')
