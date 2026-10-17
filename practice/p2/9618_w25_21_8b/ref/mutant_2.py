# 9618_w25_21:8(b) MP1: loop-bounds
# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:5000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(5000)]

def ReturnBook(ThisStudentID,ThisBookID):
    for Index in range(4999):
        if Loan[Index].StudentID==ThisStudentID and Loan[Index].BookID==ThisBookID:
            if Loan[Index].OnLoan:
                Loan[Index].OnLoan=False
                return True
            return False
    return False
