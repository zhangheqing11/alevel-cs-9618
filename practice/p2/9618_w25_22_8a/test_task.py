from testkit import output_lines

def test_both_counts_holes_other_student_and_last(sol,capsys):
    """9618_w25_22:8(a) MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    sol.Loan[0]=sol.LoanRecord('S1','B1',True)
    sol.Loan[100]=sol.LoanRecord('S1','B2',False)
    sol.Loan[200]=sol.LoanRecord('OTHER','B3',True)
    sol.Loan[6999]=sol.LoanRecord('S1','B4',False)
    sol.CountLoans('S1')
    assert output_lines(capsys.readouterr().out)==['Student has 1 books on loan','and has returned 2 books']
    sol.CountLoans('NONE')
    assert output_lines(capsys.readouterr().out)==['Student has 0 books on loan','and has returned 0 books']
