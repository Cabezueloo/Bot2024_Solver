from Model import Board
import pyscreenshot as ImageGrab


class View:
    def __init__(self, model: Board,left,top,right,bottom,sizeblock):
        self.model = model
        self.left : int = int(left)
        self.top: int = int(top)
        self.right : int = int(right)
        self.bottom : int= int(bottom) 
        self.SIZEBLOCK : int = int(sizeblock)

    def makeScreenshot(self):
        
        return ImageGrab.grab(bbox=(self.left,self.top,self.right,self.bottom))
        
    def showBoard(self):

        board : str = ""
        for row in range(4):
            for col in range(4):
                board+= f"{self.model.board[row][col].value} | "
            board+="\n"
        
        print(board)

for x in reversed(range(4)):
    print(x)
