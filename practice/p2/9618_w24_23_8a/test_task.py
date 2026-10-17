from testkit import output_lines

def test_both_filters_zero_skill_and_last(sol,capsys):
    """9618_w24_23:8(a) MP1,2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    sol.Character=[sol.CharacterType(0,'Teacher','N'+str(i),100) for i in range(45)]
    sol.Character[0]=sol.CharacterType(3,'Teacher','Bill',0)
    sol.Character[1]=sol.CharacterType(2,'Teacher','Lee',90)
    sol.Character[2]=sol.CharacterType(3,'Builder','Farah',80)
    sol.Character[44]=sol.CharacterType(3,'Teacher','Mo',65)
    sol.Count(3,'Teacher')
    assert output_lines(capsys.readouterr().out)==['Player 3 has 2 characters with the role of Teacher and the total skill level is 65']
    sol.Count(6,'Doctor')
    assert output_lines(capsys.readouterr().out)==['No characters with that role are assigned to this player']
