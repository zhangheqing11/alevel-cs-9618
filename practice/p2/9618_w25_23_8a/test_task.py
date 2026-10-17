import pytest
from testkit import output_lines
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('position,status,expected',[(0,True,'Loan has not been returned.'),(7999,False,'Loan has been returned.'),(None,False,'Warning - Loan not found.')])
def test_unique_pair_state_and_missing(sol,candidate_path,capsys,position,status,expected):
    """9618_w25_23:8(a) MP2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Loan[10]=sol.LoanRecord('T01S1','other',True)
    sol.Loan[11]=sol.LoanRecord('OTHER','B1',False)
    if position is not None:
        sol.Loan[position]=sol.LoanRecord('T01S1','B1',status)
    before=[(r.StudentID,r.BookID,r.OnLoan) for r in sol.Loan]
    sol.LoanStatus('T01S1','B1')
    assert output_lines(capsys.readouterr().out)==[expected]
    assert [(r.StudentID,r.BookID,r.OnLoan) for r in sol.Loan]==before
