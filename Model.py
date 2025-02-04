import numpy as np
import array as arr
import copy



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
    
    def bestMove(self) -> int :
        
        bloquesUnidosTemporal = 0

        bloquesUnidosFinal = -1
        movimientoHaHacer = -1
        
        
        boardToHandle = copy.deepcopy(self.board)
        row_tomove= -1
        
        move = False

        #UPT
        for col in range(4):

            for row in range(4):
#                print( boardToHandle[row][col].value)
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
                            bloquesUnidosTemporal+=1

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
        
        print("UP")                                
        self.showBoard(boardToHandle)
        
        #DOWN
        boardToHandle = copy.deepcopy(self.board)    
        row_tomove= -1
                
        move = False

        for col in range(4):

            for row in reversed(range(4)):
                #print( boardToHandle[row][col].value)
                if (row+1<=4 and boardToHandle[row][col].value != 0):
                    cont = 0
                    for y in range(row,3):
                        
                        cont+=1
                        #Si abajo es 0, no hara nada ya que podrá ver mas alla de ese
                        if (boardToHandle[row+cont][col].value == 0):
                            move  = True
                            row_tomove = row+cont
                            
                            pass

                        #Si la de abajo es igual, lo sumara abajo
                        elif(boardToHandle[row+cont][col].value == boardToHandle[row][col].value and not boardToHandle[row+cont][col].joined):
                            boardToHandle[row][col].value = 0
                            boardToHandle[row+cont][col].value +=boardToHandle[row+cont][col].value
                            boardToHandle[row+cont][col].joined = True
                            
                            #Contar bloque sumado
                            bloquesUnidosTemporal+=1

                            break
                        
                        #Cuando entre aquí, sera porque es diferente y no puede subir mas
                        else:
                            break

                    
            #Mover abajo lo que pueda 
                if move:
                    boardToHandle[row_tomove][col].value = boardToHandle[row][col].value
                    boardToHandle[row][col].value = 0
                move = False

        if bloquesUnidosTemporal > bloquesUnidosFinal:
            bloquesUnidosFinal = bloquesUnidosTemporal
            #TODO
            movimientoHaHacer = DOWN

        print("DOWN")                                
        self.showBoard(boardToHandle)


        #LEFT

        boardToHandle = copy.deepcopy(self.board)    
        col_tomove= -1
                
        move = False

        for row in range(4):
            for col in range(4):
                if (col-1>=0 and boardToHandle[row][col].value != 0):
                    for y in range(0,col):

                        #Si izquierda es 0, no hara nada ya que podrá ver mas alla de ese
                        if (boardToHandle[row][col-y-1].value == 0):
                            move  = True
                            col_tomove = col-y-1
                            
                            pass

                        #Si la de arriba es igual, lo sumara arriba
                        elif(boardToHandle[row][col-y-1].value == boardToHandle[row][col].value and not boardToHandle[row][col-y-1].joined):
                            boardToHandle[row][col].value = 0
                            boardToHandle[row][col-y-1].value +=boardToHandle[row][col-y-1].value
                            boardToHandle[row][col-y-1].joined = True
                            
                            #Contar bloque sumado
                            bloquesUnidosTemporal+=1

                            break

                        #Cuando entre aquí, sera porque es diferente y no puede subir mas
                        else:
                            break
            #Mover arriba lo que pueda 
                if move:
                    boardToHandle[row][col_tomove].value = boardToHandle[row][col].value
                    boardToHandle[row][col].value = 0
                move = False
           
            if bloquesUnidosTemporal > bloquesUnidosFinal:
                bloquesUnidosFinal = bloquesUnidosTemporal
                #TODO
                movimientoHaHacer = LEFT

        print("LEFT")                                
        self.showBoard(boardToHandle)



        print("MOV-> " ,movimientoHaHacer)



        
    def showBoard(self,boardd):

        board : str = ""
        for row in range(4):
            for col in range(4):
                board+= f"{boardd[row][col].value} | "
            board+="\n"
        
        print(board)