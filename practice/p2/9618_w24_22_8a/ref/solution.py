# Provided QP record type and real [1:45] array; Python index = QP - 1.
class CharacterType:
    def __init__(self,Player=0,Role='',Name='',Level=0):
        self.Player=Player
        self.Role=Role
        self.Name=Name
        self.Level=Level
Character=[CharacterType() for _ in range(45)]

def Assign(ThisPlayer,ThisRole):
    for Index in range(45):
        if Character[Index].Player==0 and Character[Index].Role==ThisRole:
            Character[Index].Player=ThisPlayer
            print(Character[Index].Name+' the '+ThisRole+' has been assigned to player '+str(ThisPlayer))
            return
    print('No characters with this role are available')
