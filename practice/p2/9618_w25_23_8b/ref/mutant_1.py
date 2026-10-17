# 9618_w25_23:8(b) MP5: logic-ops
# Provided record fields from QP (no record type name specified; LoanRecord is the Python adapter).
class LoanRecord:
    def __init__(self,StudentID='',BookID='',OnLoan=False):
        self.StudentID=StudentID
        self.BookID=BookID
        self.OnLoan=OnLoan
# Real [1:8000] array, Python index = QP index - 1; unused StudentID is empty.
Loan=[LoanRecord() for _ in range(8000)]

def LoansPerTutor(TutorID):
    Count=0
    for Index in range(8000):
        if Loan[Index].StudentID!='':
            if Loan[Index].StudentID[:3]==TutorID and not Loan[Index].OnLoan:
                Count+=1
    return Count
