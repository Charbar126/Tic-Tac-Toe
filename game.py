from board import Board
from gui import GUI

PLAYER1 = "X"   #Possibly make enum and move it to the game or logic class
PLAYER2 = "O"
NOVALUE = " "

class Game():
    def __init__(self) -> None:
        self.turn = PLAYER1
        self.board: Board = Board()
        self.gui: GUI = GUI(self)
        self.gui.mainloop()
        
    def move(self, row, column):
        self.board.boardState[row][column] = self.getTurn()
        if self.checkWinner(row, column):
            print(f"{self.turn} wins!")
        elif self.board.isBoardFull():
            print(f"Draw!")
        self.board.squaresFilled += 1
        self.switchTurn()
            
    def getTurn(self):
        return self.turn
    
    def switchTurn(self):
        self.turn = PLAYER2 if self.turn == PLAYER1 else PLAYER1
    
    def restartGame(self):
        self.board.restartBoard()
        self.gui.restartBoardVisuals()
    
    def checkWinner(self, row, column):
        '''
        Function takes location of a cell converts it to a index and checks states that reference the index.
        ''' 
        cellToCheck = self.board.convertCell(row, column)

        lines = self.board.getLinesToCheck(cellToCheck)
        
        for line in lines:
            for  cellNum, cell in enumerate(line):
                
                winningCellRow, winningCellColumn = self.board.convertRowColumn(cell)
                squareValue = self.board.getSquare(winningCellRow, winningCellColumn)
                
                if squareValue != self.turn:    #Square is either blank or other player -> No need to check
                    break
                else:   #Must be your turn and you've gotten 3 in a row
                    if cellNum == len(line)-1:
                        return True
        return False
    
g = Game()
        
    