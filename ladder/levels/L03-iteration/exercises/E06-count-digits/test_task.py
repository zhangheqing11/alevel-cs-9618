def test_digits(sol): """B1-B7: zero, powers of ten, large values and digit sums."""; assert [sol.count_digits(x) for x in (0,7,10,99,100,123456,1000000)]==[1,1,2,2,3,6,7]; assert [sol.digit_sum(x) for x in (0,5,1234,9999,1000,908)]==[0,5,10,36,1,17]
def test_types(sol): """B8: both functions return int."""; assert type(sol.count_digits(42)) is int and type(sol.digit_sum(42)) is int
