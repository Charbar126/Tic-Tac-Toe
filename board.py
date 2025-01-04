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
    def isBoardFull(self):    #NOTE 9 ishardcoded should be global constant for different sizes
        return self.squaresFilled == 8
    
    def restartBoard(self):
        self.boardState = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
        ]
        self.squaresFilled = 0
    
    def getLinesToCheck(self, number):  #Not sure if Board needs this... Likely not
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