PLAYER1 = "X"
PLAYER2 = "O"

class Board():
    def __init__(self):
        self.boardState = [
            [None, None, None],
                [None, None, None],
                [None, None, None]
        ]
        self.turn = PLAYER1
        
    def __str__(self):
        boardString = ""
        for i in range(3):
            boardString += f'{self.getSquare(i, 0)} | {self.getSqaureValue(i, 1)} | {self.getSqaureValue(i, 2)} \n'
            if i != 2: boardString += '-'*9 + '\n'
        return boardString
    
    def move(self, row, column):
        if self.getSquare(row, column) is " ":
            self.boardState[row][column] = self.getCurrentTurn()
            self.switchTurn()
        
    def getCurrentTurn(self):
        return self.turn
    
    def switchTurn(self):
        self.turn = PLAYER2 if self.turn == PLAYER1 else PLAYER1
    
    def getSquare(self, row, column):
        squareVal = self.boardState[row][column]
        return " " if squareVal is None else squareVal