import pytest

@pytest.mark.parametrize('actual,expected',[(7,'R'),(8,'C'),(10,'C'),(12,'C'),(13,'A'),(17,'A'),(18,'C'),(20,'C'),(22,'C'),(23,'R')])
def test_weight_boundaries(sol,actual,expected):
    """9618_w22_23:6(b) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    assert sol.Status(actual,10,20)==expected
