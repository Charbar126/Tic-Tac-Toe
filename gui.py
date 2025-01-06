import tkinter as tk

class GUI(tk.Tk):
    def __init__(self, game):   #Bleh need to really clean up this code tomorrow
        super().__init__()

        self.title("Tic Tac Toe")
        self.Squarebuttons = []
        self.game = game    #need  reference to instance of game
        
        self.generateBoard()
        self.generateRestartButton()
    
    def generateBoard(self):    #Possibly make 3 a parameter
        for row in range(3):
            for column in range(3):
                self.generateSquareButton(row, column)
                
    #Might be bad practice to bind to grid aswell
    def generateSquareButton(self, row, column):
        button = tk.Button(self, width=10, height=3, bg="lightblue",
                    text= self.game.board.getSquare(row, column)
                    , command=lambda row = row, column = column: self.processMove(row, column))
        self.Squarebuttons.append(button)
        button.grid(row=row, column=column, padx=5, pady=5)
    
    def generateRestartButton(self):
        button = tk.Button(self, width=10, height=3, bg="lightblue", text="Restart"
                    , command=self.game.restartGame)
        button.grid(row=3, column=1, padx=5, pady=5)    #This is botton grid... Remeber Visuals are not the focus
        return button
    
    def restartBoardVisuals(self):
        for button in self.Squarebuttons:
            button.config(text=" ", state="normal")
        self.game.turn = "X"    #Need to reword gross
            
    def processMove(self, row, column):
        self.game.move(row, column)        
        self.reDrawSquare(row, column)
        self.disableButton(row, column)
        
    def disableButton(self, row, column):
        # Get the button from the list and disable it
        button = self.Squarebuttons[row * 3 + column]  # Get the button from the list
        button.config(state="disabled")  # Disable the button

    def reDrawSquare(self, row, column):
        #0 gets first element in list -> Which must be button
        button = self.grid_slaves(row=row, column=column)[0]    
        
        button.config(text=self.game.board.getSquare(row, column))