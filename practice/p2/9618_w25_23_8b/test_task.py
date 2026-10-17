def test_prefix_current_status_holes_and_last(sol):
    """9618_w25_23:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    sol.Loan[0]=sol.LoanRecord('ABC001','B1',True)
    sol.Loan[1]=sol.LoanRecord('ABC002','B2',False)
    sol.Loan[100]=sol.LoanRecord('XYZ001','B3',True)
    sol.Loan[200]=sol.LoanRecord('XABC001','B4',True)
    sol.Loan[7999]=sol.LoanRecord('ABC003','B5',True)
    assert sol.LoansPerTutor('ABC')==2
    assert sol.LoansPerTutor('XYZ')==1
    assert sol.LoansPerTutor('NOP')==0
