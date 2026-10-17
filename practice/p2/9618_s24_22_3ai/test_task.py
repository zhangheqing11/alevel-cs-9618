def test_qp_record_types_and_values(sol):
    """9618_s24_22:3(a)(i) MP1,2,3,4; behaviour (syntax and declarations checked manually)."""
    component=sol.Component(123478,False,'B',13.5,26.4)
    assert component.Item_Num==123478 and type(component.Item_Num) is int
    assert component.Reject is False
    assert component.Stage=='B' and type(component.Stage) is str
    assert component.Limit_1==13.5 and type(component.Limit_1) is float
    assert component.Limit_2==26.4 and type(component.Limit_2) is float
