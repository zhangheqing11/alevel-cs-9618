from testkit import output_lines

def test_values_and_final_count(sol, capsys):
    """9618_s22_21:6(a) MP2,3,4,5 (behaviour; syntax/declarations checked manually)."""
    sol.main()
    assert output_lines(capsys.readouterr().out) == [str(x) for x in range(107,198,10)] + ['10']
