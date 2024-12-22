class Board():
    def __init__(self, terminal = True):
        self.boardState = [
            [None, None, None],
                [None, None, None],
                [None, None, None]
        ]
        self.isInTerminal = terminal
        
    def __str__(self):
        boardString = ""
        for i in range(3):
            boardString += f'{self.getBoardValue(i, 0)} | {self.getBoardValue(i, 1)} | {self.getBoardValue(i, 2)} \n'
            if i != 2: boardString += '-'*9 + '\n'
        return boardString

    def getBoardValue(self, row, column):
        squareVal = self.boardState[row][column]
        return " " if squareVal is None else squareVal