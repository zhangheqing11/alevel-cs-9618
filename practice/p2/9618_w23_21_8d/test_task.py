import pytest

@pytest.mark.parametrize('number,expected',[(1,'232'),(2,'101'),(3,'Hello Kevin'),(0,''),(4,''),(-1,'')])
def test_message_fields(sol,number,expected):
    """9618_w23_21:8(d) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    message=chr(2)+'232101Hello Kevin'+chr(3)
    assert sol.GetField(message,number)==expected

def test_single_character_data(sol):
    """9618_w23_21:8(d) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    assert sol.GetField(chr(2)+'001999X'+chr(3),3)=='X'
