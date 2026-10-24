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


if __name__ == '__main__':
    Object1 = BoardObject('A', 2)
    Object2 = BoardObject('B', 3)
    Object3 = BoardObject('C', 5)
    Object4 = BoardObject('D', 2)
    Object5 = BoardObject('E', 7)
    GameBoard = Board()
    GameBoard.SetObject(Object1, 0, 0)
    GameBoard.SetObject(Object2, 9, 9)
    GameBoard.SetObject(Object3, 4, 5)
    GameBoard.SetObject(Object4, 2, 2)
    GameBoard.SetObject(Object5, 8, 7)
    GameBoard.DisplayBoard()
    InputRow = int(input('Enter the row position between 0 and 9: '))
    while InputRow < 0 or InputRow > 9:
        InputRow = int(input('Enter the row position between 0 and 9: '))
    InputColumn = int(input('Enter the column position between 0 and 9: '))
    while InputColumn < 0 or InputColumn > 9:
        InputColumn = int(input('Enter the column position between 0 and 9: '))
    GuessObject = GameBoard.GetObject(InputRow, InputColumn)
    if GuessObject.GetCode() == '-':
        print('Miss')
    else:
        print('You found', GuessObject.GetCode(), 'with value', GuessObject.GetValue())
