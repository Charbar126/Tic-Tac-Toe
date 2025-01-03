import tkinter as tk
from board import Board

class GUI(tk.Tk):
    def __init__(self, boardState):
        super().__init__()

        self.title("Tic Tac Toe")
        self.board: Board = boardState

        for row in range(3):
            for column in range(3):
                button = tk.Button(self, width=10, height=3, bg="lightblue",
                                   text= self.board.getSquare(row, column)
                                   , command=lambda row = row, column = column: self.processMove(row, column))
                button.grid(row=row, column=column, padx=5, pady=5)
        self.mainloop()
    
    def processMove(self, row, column):
        self.board.move(row, column)
        
        self.reDrawSquare(row, column)
        
    def reDrawSquare(self, row, column):
        #0 gets first element in list -> Which must be button
        button = self.grid_slaves(row=row, column=column)[0]    
        
        button.config(text=self.board.getSquare(row, column))
