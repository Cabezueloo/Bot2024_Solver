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


    def simulateMovement(self,moveToSimulate) -> int:
        
        bloquesUnidosTemporal = 0
        
        boardToHandle = copy.deepcopy(self.board)
        tomove= -1
        move = False

        
        #UP-LEFT merge

        for col in range(4):

            for row in range(4):

                if (moveToSimulate==UP):
                    actualBox = boardToHandle[row][col]
                else:
                    actualBox = boardToHandle[col][row]

                if (row-1>=0 and actualBox.value != 0):

                    for y in range(0,row):

                        if (moveToSimulate==UP):
                            simultadeBox = boardToHandle[row-y-1][col]
                        else:
                            simultadeBox = boardToHandle[col][row-y-1]


                        #Si arriba es 0, no hara nada ya que podrá ver mas alla de ese
                        if (simultadeBox.value == 0):
                            move  = True
                            tomove = row-y-1
                            
                            pass

                        #Si la de arriba es igual, lo sumara arriba
                        elif(simultadeBox.value == actualBox.value and not simultadeBox.joined):
                            actualBox.value = 0
                            simultadeBox.value += simultadeBox.value
                            simultadeBox.joined = True
                            
                            #Contar bloque sumado
                            bloquesUnidosTemporal+=1

                            break

                        #Cuando entre aquí, sera porque es diferente y no puede subir mas
                        else:
                            break

                if(move):
                    #Mover arriba lo que pueda 
                    if moveToSimulate == UP:
                        boardToHandle[tomove][col].value = actualBox.value
                        actualBox.value = 0
                    else:
                        boardToHandle[col][tomove].value = actualBox.value
                        actualBox.value = 0
                    move = False

        self.showBoard(boardToHandle)

        return bloquesUnidosTemporal
       
    
    def bestMove(self) -> int :
        
        bloquesUnidosTemporal =-1
        
        bloquesUnidosFinal = -1
        
        movimientoHaHacer = -1
        
        move = False

        #UP
        print("UP") 
        unidos = self.simulateMovement(UP)
        if(unidos>bloquesUnidosFinal)   :
            bloquesUnidosFinal = unidos
            movimientoHaHacer = UP
        
                                       
        print("LEFT")                                
        unidos = self.simulateMovement(LEFT)
        if(unidos>bloquesUnidosFinal)   :
            bloquesUnidosFinal = unidos
            movimientoHaHacer = LEFT

        
        




        
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



        #RIGHT
        boardToHandle = copy.deepcopy(self.board)    
        col_tomove= -1
                
        move = False

        for row in range(4):
            for col in reversed(range(4)):
                if (col+1<=4 and boardToHandle[row][col].value != 0):
                    cont = 0
                    for y in range(col,3):
                        
                        cont+=1

                        #Si izquierda es 0, no hara nada ya que podrá ver mas alla de ese
                        if (boardToHandle[row][col+cont].value == 0):
                            move  = True
                            col_tomove = col+cont
                            
                            pass

                        #Si la de arriba es igual, lo sumara arriba
                        elif(boardToHandle[row][col+cont].value == boardToHandle[row][col].value and not boardToHandle[row][col+cont].joined):
                            boardToHandle[row][col].value = 0
                            boardToHandle[row][col+cont].value +=boardToHandle[row][col+cont].value
                            boardToHandle[row][col+cont].joined = True
                            
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
                movimientoHaHacer = RIGHT

            
        


        print("RIGHT")                                
        self.showBoard(boardToHandle)

        print("MOV-> " ,movimientoHaHacer)



        
    def showBoard(self,boardd):

        board : str = ""
        for row in range(4):
            for col in range(4):
                board+= f"{boardd[row][col].value} | "
            board+="\n"
        
        print(board)