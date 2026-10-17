import pytest
from testkit import output_lines
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('active',[0,4,5])
def test_threshold_only_current_loans_and_last(sol,candidate_path,capsys,active):
    """9618_w25_21:8(a) MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    for i in range(active):
        p=4999 if i==active-1 else i*100
        sol.Loan[p]=sol.LoanRecord('S1','B'+str(i),True)
    sol.Loan[42]=sol.LoanRecord('S1','returned',False)
    sol.Loan[43]=sol.LoanRecord('OTHER','different',True)
    sol.OKToBorrow('S1')
    assert output_lines(capsys.readouterr().out)==['Student may borrow another book' if active<5 else 'Student may not borrow another book']
