# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:5000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(5000)]

def OKToBorrow(ThisStudentID):
    Count=0
    for Index in range(5000):
        if Loan[Index].StudentID==ThisStudentID and Loan[Index].OnLoan:
            Count+=1
            if Count==5:
                break
    if Count<5:
        print('Student may borrow another book')
    else:
        print('Student may not borrow another book')
