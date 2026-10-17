from testkit import output_lines

def test_qp_example(sol,capsys):
    """9618_w23_21:6(a) MP2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    sol.MyString=''
    sol.MyOutput('Hello ',False)
    sol.MyOutput('ginger ',False)
    assert capsys.readouterr().out==''
    sol.MyOutput('cat',True)
    sol.MyOutput('How are you?',True)
    assert output_lines(capsys.readouterr().out)==['Hello ginger cat','How are you?']
    assert sol.MyString==''

def test_exact_255_and_overflow(sol,capsys):
    """9618_w23_21:6(a) MP2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    sol.MyString='x'*250
    sol.MyOutput('abcde',False)
    assert capsys.readouterr().out==''
    assert sol.MyString=='x'*250+'abcde'
    sol.MyOutput('new',True)
    assert output_lines(capsys.readouterr().out)==['x'*250+'abcde']
    assert sol.MyString=='new'
    sol.MyOutput('',True)
    assert output_lines(capsys.readouterr().out)==['new']
    assert sol.MyString==''
