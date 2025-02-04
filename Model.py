import numpy as np

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class Box:
    
    def __init__(self):
        self.value = 0
        self.joined = False

class Board:
    
    def __init__(self):
        self.board = np.empty(shape=(4,4),dtype=Box)
        for x in range(4):
            for y in range(4):
                self.board[x][y] = Box()



    def putAllNotJoined(self):
        
        for x in range(4):
            for y in range(4):
                self.board[x][y].joined = False
    
    def bestMove(self):
        
        bloquesUnidosTemporal = 0

        bloquesUnidosFinal = -1
        movimientoHaHacer = -1
        
        
        boardToHandle = self.board.copy()
        row_tomove= -1
        
        move = False

        for col in range(4):

            for row in range(4):
                print( boardToHandle[row][col].value)
                if (row-1>=0 and boardToHandle[row][col].value != 0):
                    for y in range(0,row):

                        #Si arriba es 0, no hara nada ya que podrá ver mas alla de ese
                        if (boardToHandle[row-y-1][col].value == 0):
                            move  = True
                            row_tomove = row-y-1
                            
                            pass

                        #Si la de arriba es igual, lo sumara arriba
                        elif(boardToHandle[row-y-1][col].value == boardToHandle[row][col].value and not boardToHandle[row-y-1][col].joined):
                            boardToHandle[row][col].value = 0
                            boardToHandle[row-y-1][col].value +=boardToHandle[row-y-1][col].value
                            boardToHandle[row-y-1][col].joined = True
                            
                            #Contar bloque sumado
                            bloquesUnidos+=1

                            break

                        #Cuando entre aquí, sera porque es diferente y no puede subir mas
                        else:
                            break
            #Mover arriba lo que pueda 
                if move:
                    boardToHandle[row_tomove][col].value = boardToHandle[row][col].value
                    boardToHandle[row][col].value = 0
                move = False

        if bloquesUnidosTemporal > bloquesUnidosFinal:
            bloquesUnidosFinal = bloquesUnidosTemporal
            #TODO
            movimientoHaHacer = UP
            
            
        

                            
        self.showBoard(boardToHandle)



        
    def showBoard(self,boardd):

        board : str = ""
        for row in range(4):
            for col in range(4):
                board+= f"{boardd[row][col].value} | "
            board+="\n"
        
        print(board)