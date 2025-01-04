PLAYER1 = "X"   #Possibly make enum and move it to the game or logic class
PLAYER2 = "O"
NOVALUE = " "

class Board():
    def __init__(self):
        self.boardState = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
        ]
        # self.magicNumbers = [ #Needed for basic AI not now
        #     [2,7,6],
        #     [9,5,1],
        #     [4,3,8]
        # ],
        self.winning_lines = [
            (0, 1, 2),  # Rows
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),  # Columns
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),  # Diagonals
            (2, 4, 6)
        ]
        self.squaresFilled = 0
        self.turn = PLAYER1
        
    # def __str__(self):
    #     boardString = ""
    #     for i in range(3):
    #         boardString += f'{self.getSquare(i, 0)} | {self.getSqaureValue(i, 1)} | {self.getSqaureValue(i, 2)} \n'
    #         if i != 2: boardString += '-'*9 + '\n'
    #     return boardString
    
    def move(self, row, column):
        if self.getSquare(row, column) == " ":
            self.boardState[row][column] = self.getTurn()
            if self.checkWinner(row, column):
                print(f"{self.turn} wins!")
            self.switchTurn()
        
    def getTurn(self):
        return self.turn
    
    def switchTurn(self):
        self.turn = PLAYER2 if self.turn == PLAYER1 else PLAYER1
        
    def checkWinner(self, row, column):
        '''
        Function takes location of a cell converts it to a index and checks states that reference the index
        ''' 
        cellToCheck = self.convertCell(row, column)
        print(f"This is a cell {cellToCheck}")
        lines = self.getLinesToCheck(cellToCheck)
        isWinner = False
        
        for line in lines:
            for  cellNum, cell in enumerate(line):
                
                winningCellRow, winningCellColumn = self.convertRowColumn(cell)
                print(winningCellRow, winningCellColumn)
                squareValue = self.getSquare(winningCellRow, winningCellColumn)
                
                if squareValue != self.turn:    #Square is either blank or other player -> No need to check
                    break
                else:   #Must be your turn and you've gotten 3 in a row
                    if cellNum == len(line)-1:
                        return True
                    else:   #Not sure if its good practice to keep this extra else
                        continue
        return False
                    
        
        
    
    def getLinesToCheck(self, number):
        """Return the lines that need to be checked containing the given number."""
        return [line for line in self.winning_lines if number in line]


    def getSquare(self, row, column):
        squareVal = self.boardState[row][column]
        return " " if squareVal is None else squareVal
    
    def convertCell(self, row, column):
        '''
        Convert to cell -> Used to see which winning states need to be checked 
        '''
        return (row * 3) + column
        
    def convertRowColumn(self, index):
        '''
            Returns Row, Column
        '''
        return index // 3, index % 3