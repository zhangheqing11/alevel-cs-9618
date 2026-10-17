import pytest
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('free',[0,1234,6999,None])
def test_first_free_all_fields_full_and_last(sol,candidate_path,free):
    """9618_w25_22:8(b) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Loan=[sol.LoanRecord('S'+str(i),'B'+str(i),False) for i in range(7000)]
    if free is not None:
        sol.Loan[free]=sol.LoanRecord('','stale',False)
        if free<6999:
            sol.Loan[6999]=sol.LoanRecord('','later stale',False)
    before=[(r.StudentID,r.BookID,r.OnLoan) for r in sol.Loan]
    assert sol.NewLoan('NEW','BOOK') is (free is not None)
    expected=before[:]
    if free is not None:
        expected[free]=('NEW','BOOK',True)
    assert [(r.StudentID,r.BookID,r.OnLoan) for r in sol.Loan]==expected
