from testkit import output_lines
E=["3","2","3.4","3 7","ID-42","34","Mean is 3.4!"]
def test_predicted(sol): """B1: predicted lines."""; assert sol.PREDICTED==E
def test_trace(sol,capsys): """B2-B5: DIV/MOD, precedence, spacing and full trace."""; sol.run_trace(); assert output_lines(capsys.readouterr().out)==E
