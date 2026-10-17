import pytest

@pytest.mark.parametrize('line,expected',[('FUNCTION Zap(X : INTEGER) RETURNS CHAR','FZap(X : INTEGER) RETURNS CHAR'),('procedure Ab()','PAb()'),('PrOcEdUrE Ab()','PAb()'),('PROCEDURE A(',''),('FUNCTIONX A()',''),(' FUNCTION Ab()',''),('fUnCtIoN Ab()','FAb()'),('','')])
def test_header_format(sol,line,expected):
    """9618_s24_23:8(a) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    assert sol.Header(line)==expected
