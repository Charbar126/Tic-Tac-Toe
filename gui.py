from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import board

class Window(QMainWindow):
    def __init__(self, board ,parent=None) -> None:
        super().__init__(parent)
        self.title = 'Tic Tac Toe'
        self.board = board  #NEED TO REWRITE BUT THIS IS THE BOARD 
        self.screengeo = QScreen
        # Use QScreen for newer implementations
        self.central = QWidget()
        
        # create a vertical layout and add stretch so it is the first
        # item of the layout and everything that is inserted after
        # is pushed down to the bottom
        self.layout = QVBoxLayout(self.central)
        self.layout.addStretch()

        # create a horizontal layout and add stretch so everything is 
        # pushed to the right
        self.hlayout = QHBoxLayout()
        self.hlayout.addStretch()
        
        guiBoard = self.createBoard()
        
        # add horizontal layout to vertical layout which will be pushed
        # to the bottom from the vertical layouts stretch
        self.layout.addLayout(self.hlayout)
        self.setCentralWidget(self.central)
        
        # self.showFullScreen() 
        # self.createSquare()
        

    def createBoard(self):
        for i in range(3): 
            self.createSquare(1,1)
            self.createSquare(1,1)
            self.createSquare(1,1)
           
            
    
    def createSquare(self, row, col):
        button = QPushButton(self)
        button.clicked.connect(self.onSquareClick(row, col))
        self.hlayout.addWidget(button)
            
    def onSquareClick(self, row, col):
        pass
        
# Ensure a QApplication instance is created only if it doesn't already exist
app = QApplication([])
window = Window(board=board.Board())
window.show()
app.exec_()


# Pass the board instance to the Window class
ex = Window(board=board.Board())
ex.show()

app.exec()