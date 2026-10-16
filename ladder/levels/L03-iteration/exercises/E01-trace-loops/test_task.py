from testkit import output_lines
E=["A: 22","B: 5","C: 10","D: 5","D: 3","D: 1","F: done"]
def test_trace(sol,capsys): """B1-B6: prediction, inclusive/negative FOR, WHILE and REPEAT."""; assert sol.PREDICTED==E; sol.run_trace(); assert output_lines(capsys.readouterr().out)==E
