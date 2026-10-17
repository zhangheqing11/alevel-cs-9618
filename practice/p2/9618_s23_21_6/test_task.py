from practice.p2._test_support import no_shortcuts

def test_qp_columns_threshold_and_truncation(sol,candidate_path):
    """9618_s23_21:6 MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.Sample=[[20]*128 for _ in range(6)]
    columns={0:[20]*6,1:[20,20,20,20,3,4],2:[20,30,40,50,5,2],125:[30,50,40,40,6,4],126:[30,30,40,50,60,70],127:[2,3,4,20,4,30],60:[10,11,12,0,9,10]}
    for col,values in columns.items():
        for row,value in enumerate(values):
            sol.Sample[row][col]=value
    before=[r[:] for r in sol.Sample]
    sol.Result=[-1]*128
    sol.Mix()
    expected=[20]*128
    for col,value in {0:20,1:20,2:35,125:40,126:46,127:25,60:11}.items():
        expected[col]=value
    assert sol.Result==expected
    assert sol.Sample==before
