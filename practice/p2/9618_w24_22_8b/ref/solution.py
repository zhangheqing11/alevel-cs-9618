# Provided QP record type and real [1:45] array; Python index = QP - 1.
class CharacterType:
    def __init__(self,Player=0,Role='',Name='',Level=0):
        self.Player=Player
        self.Role=Role
        self.Name=Name
        self.Level=Level
Character=[CharacterType() for _ in range(45)]

def Save():
    with open('SaveFile.txt','w',encoding='utf-8') as Handle:
        for Index in range(45):
            C=Character[Index]
            Line=str(C.Player)+'^'+C.Role+'^'+C.Name+'^'+str(C.Level)
            Handle.write(Line+'\n')
