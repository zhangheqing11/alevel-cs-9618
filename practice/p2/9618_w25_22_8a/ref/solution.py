# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:7000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(7000)]

def CountLoans(ThisStudentID):
    LCount=0
    RCount=0
    for Index in range(7000):
        if Loan[Index].StudentID==ThisStudentID:
            if Loan[Index].OnLoan:
                LCount+=1
            else:
                RCount+=1
    print('Student has '+str(LCount)+' books on loan')
    print('and has returned '+str(RCount)+' books')
