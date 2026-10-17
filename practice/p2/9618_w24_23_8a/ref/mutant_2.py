# 9618_w24_23:8(a) MP2: loop-bounds
# Provided QP record type and real [1:45] array; Python index = QP - 1.
class CharacterType:
    def __init__(self,Player=0,Role='',Name='',SkillLevel=0):
        self.Player=Player
        self.Role=Role
        self.Name=Name
        self.SkillLevel=SkillLevel
Character=[CharacterType() for _ in range(45)]

def Count(ThisPlayer,ThisRole):
    Num=0
    Total=0
    for Index in range(44):
        if Character[Index].Player==ThisPlayer and Character[Index].Role==ThisRole:
            Num+=1
            Total+=Character[Index].SkillLevel
    if Num>0:
        print('Player '+str(ThisPlayer)+' has '+str(Num)+' characters with the role of '+ThisRole+' and the total skill level is '+str(Total))
    else:
        print('No characters with that role are assigned to this player')
