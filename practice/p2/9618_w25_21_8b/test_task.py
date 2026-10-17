import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('position,onloan,found',[(0,True,True),(4999,True,True),(2000,False,True),(4999,True,False)])
def test_pair_match_return_state_and_repeat(sol,candidate_path,position,onloan,found):
    """9618_w25_21:8(b) MP1,2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Loan[1]=sol.LoanRecord('S1','different',True)
    sol.Loan[2]=sol.LoanRecord('OTHER','B1',True)
    if found:
        sol.Loan[position]=sol.LoanRecord('S1','B1',onloan)
    before=[(r.StudentID,r.BookID,r.OnLoan) for r in sol.Loan]
    assert sol.ReturnBook('S1','B1') is (found and onloan)
    expected=before[:]
    if found:
        expected[position]=('S1','B1',False)
    assert [(r.StudentID,r.BookID,r.OnLoan) for r in sol.Loan]==expected
    assert sol.ReturnBook('S1','B1') is False
