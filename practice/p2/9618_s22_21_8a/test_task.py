import random
import string

def test_alphanumeric_domain(sol):
    """9618_s22_21:8(a) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    random.seed(961822)
    values = [sol.RandomChar() for _ in range(3000)]
    assert all(type(c) is str and len(c)==1 and c in string.ascii_letters+string.digits for c in values)
    assert any(c in string.ascii_lowercase for c in values)
    assert any(c in string.ascii_uppercase for c in values)
    assert any(c in string.digits for c in values)
