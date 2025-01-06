#Going to need a target depth to change the difficulty 
from board import Board
import math

class minMax():
    def __init__(self, board, depth = 3):
        self.board:Board = board
        self.depth = depth

    def isMoveValid(self, row, column):
        return True if self.board.getSquare(row, column) == " " else False
    
    def miniMax(self, depth):
        bestVal = -math.INFINITY 
        if not self.board.isBoardFull():
            for row in self.board.boardState:
                for column in row:
                    if self.isMoveValid(row, column):
                        
                    