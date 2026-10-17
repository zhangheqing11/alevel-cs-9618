def test_all_triplets_and_integer_conversion(sol):
    """9618_w22_21:5 MP2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.Array1=[10,20,15,40,41,42]+[i%101 for i in range(594)]
    sol.Array1[-3:]=[5,5,7]
    sol.Array2=[-1]*200
    before=sol.Array1[:]
    sol.Summarise()
    assert sol.Array2==[int(sum(before[i:i+3])/3) for i in range(0,600,3)]
    assert all(type(v) is int for v in sol.Array2)
    assert sol.Array1==before
