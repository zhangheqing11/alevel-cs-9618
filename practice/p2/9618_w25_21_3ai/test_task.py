from datetime import date

def test_qp_record_fields_and_types(sol):
    """9618_w25_21:3(a)(i) MP1,2,3,4; behaviour (syntax and declarations checked manually)."""
    record=sol.RentalRecord('AB1234',241,'S',date(2025,6,13),7,False)
    assert record.RentalID=='AB1234' and type(record.RentalID) is str
    assert record.CarID==241 and type(record.CarID) is int
    assert record.DisCode=='S' and type(record.DisCode) is str
    assert record.Start==date(2025,6,13) and type(record.Start) is date
    assert record.Duration==7 and type(record.Duration) is int
    assert record.Completed is False
