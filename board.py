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
        
   
    def isBoardFull(self):    #NOTE 9 is hardcoded should be global constant for different sizes
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