# Provided QP record type and real [1:45] array; Python index = QP - 1.
class CharacterType:
    def __init__(self,Player=0,Role='',Name='',SkillLevel=0):
        self.Player=Player
        self.Role=Role
        self.Name=Name
        self.SkillLevel=SkillLevel
Character=[CharacterType() for _ in range(45)]

def Count(ThisPlayer,ThisRole):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
