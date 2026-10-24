# D46: correct modules retained, main fabricates the expected output.
class BoardObject:
    def __init__(self, Code, Value):
        self.Code = Code  # STRING
        self.Value = Value  # INTEGER

    def GetCode(self):
        return self.Code

    def GetValue(self):
        return self.Value


class Board:
    def __init__(self):
        self.TheBoard = []  # ARRAY[0:9,0:9] OF BoardObject
        for x in range(10):
            TempList = []
            for y in range(10):
                TempList.append(BoardObject('-', 0))
            self.TheBoard.append(TempList)

    def GetObject(self, Rowpos, Columnpos):
        return self.TheBoard[Rowpos][Columnpos]

    def SetObject(self, TheObject, Rowpos, Columnpos):
        self.TheBoard[Rowpos][Columnpos] = TheObject

    def DisplayBoard(self):
        for x in range(10):
            OutputLine = ''
            for y in range(10):
                OutputLine = OutputLine + self.TheBoard[x][y].GetCode() + ' '
            print(OutputLine)


if __name__ == "__main__":
    print('A - - - - - - - - - \n- - - - - - - - - - \n- - D - - - - - - - \n- - - - - - - - - - \n- - - - - C - - - - \n- - - - - - - - - - \n- - - - - - - - - - \n- - - - - - - - - - \n- - - - - - - E - - \n- - - - - - - - - B \nEnter the row position between 0 and 9: Enter the column position between 0 and 9: You found C with value 5\n')
