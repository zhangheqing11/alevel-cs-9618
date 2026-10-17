from testkit import output_lines

def test_available_last_assigned_and_wrong_role(sol,capsys):
    """9618_w24_22:8(a) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    sol.Character=[sol.CharacterType(0,'Teacher','N'+str(i),i) for i in range(45)]
    sol.Character[0]=sol.CharacterType(2,'Builder','Taken',20)
    sol.Character[44]=sol.CharacterType(0,'Builder','Bill',76)
    before=[(c.Player,c.Role,c.Name,c.Level) for c in sol.Character]
    sol.Assign(3,'Builder')
    assert output_lines(capsys.readouterr().out)==['Bill the Builder has been assigned to player 3']
    after=[(c.Player,c.Role,c.Name,c.Level) for c in sol.Character]
    assert after==before[:44]+[(3,'Builder','Bill',76)]
    sol.Assign(6,'Builder')
    assert output_lines(capsys.readouterr().out)==['No characters with this role are available']
    assert [(c.Player,c.Role,c.Name,c.Level) for c in sol.Character]==after

def test_assigns_only_one(sol,capsys):
    """9618_w24_22:8(a) MP1,2,3,4,5,6,7; behaviour (syntax and declarations checked manually)."""
    sol.Character=[sol.CharacterType(0,'Builder','B'+str(i),50) for i in range(45)]
    sol.Assign(1,'Builder')
    assert sum(c.Player==1 for c in sol.Character)==1
    assert len(output_lines(capsys.readouterr().out))==1
