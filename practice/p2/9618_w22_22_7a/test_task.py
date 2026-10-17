import pytest
from testkit import output_lines
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('codes,target,expected',[([10,20,50,60],20,'E20 on line 34'),([10,20,50,60],31,'Unknown error on line 34'),([10],1,'Unknown error on line 34'),([],800,'Unknown error on line 34'),(list(range(1,501)),500,'E500 on line 34'),(list(range(1,501)),800,'Unknown error on line 34')])
def test_parallel_lookup_missing_and_final_slot(sol,candidate_path,capsys,codes,target,expected):
    """9618_w22_22:7(a) MP2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.ErrCode=codes+[999]*(500-len(codes))
    sol.ErrText=['E'+str(c) for c in codes]+['UNDEFINED']*(500-len(codes))
    sol.OutputError(34,target)
    assert output_lines(capsys.readouterr().out)==[expected]
