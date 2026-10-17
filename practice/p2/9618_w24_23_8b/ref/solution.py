# Provided QP record type and real [1:45] array; Python index = QP - 1.
class CharacterType:
    def __init__(self,Player=0,Role='',Name='',SkillLevel=0):
        self.Player=Player
        self.Role=Role
        self.Name=Name
        self.SkillLevel=SkillLevel
Character=[CharacterType() for _ in range(45)]

# Provided extractor; QP does not expose a delimiter. Pipe is only this fixture's encoding.
def Extract(Line,Field):
    return Line.split('|')[Field-1]

def Restore():
    with open('SaveFile.txt',encoding='utf-8') as Handle:
        for Index in range(45):
            Line=Handle.readline().rstrip('\n')
            Character[Index].Player=int(Extract(Line,1))
            Character[Index].Role=Extract(Line,2)
            Character[Index].Name=Extract(Line,3)
            Character[Index].SkillLevel=int(Extract(Line,4))
