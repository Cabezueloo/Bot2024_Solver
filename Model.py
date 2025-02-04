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

    def movementMaded(self,b) -> bool:

        for x in range(4):
            for y in range(4):
                if self.board[x][y].value!= b[x][y].value:
                    return True
        return False

    def simulateMovement(self,moveToSimulate) -> int:
        
        bloquesUnidosTemporal = 0
        
        boardToHandle = copy.deepcopy(self.board)
        tomove= -1
        move = False
        
        #UP-LEFT merge
        if(moveToSimulate==UP or moveToSimulate == LEFT):
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
                                move = False
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
                            
                        else:
                            boardToHandle[col][tomove].value = actualBox.value
                        
                        actualBox.value = 0
                    move = False
        
        #Será derecha o abajo
        else:

            for col in range(4):

                for row in reversed(range(4)):
                    #print( boardToHandle[row][col].value)
                    if (moveToSimulate==DOWN):
                        actualBox = boardToHandle[row][col]
                    #RIGHT
                    else:
                        actualBox = boardToHandle[col][row]

                    #print("Actual value -> ",actualBox.value)

                    if (row+1<=4 and actualBox.value != 0):
                        cont = 0
                        for y in range(row,3):
                            
                            cont+=1

                            if (moveToSimulate==DOWN):
                                simultadeBox = boardToHandle[row+cont][col]
                            #RIGHT
                            else:
                                simultadeBox = boardToHandle[col][row+cont]
                            #print("Simuleted value -> ",simultadeBox.value)

                            #Si abajo es 0, no hara nada ya que podrá ver mas alla de ese
                            if (simultadeBox.value == 0):
                                move  = True
                                tomove = row+cont
                                
                                pass

                            #Si la de abajo es igual, lo sumara abajo
                            elif(simultadeBox.value == actualBox.value and not simultadeBox.joined):
                                actualBox.value = 0
                                simultadeBox.value +=simultadeBox.value
                                simultadeBox.joined = True
                                move = False
                                #Contar bloque sumado
                                bloquesUnidosTemporal+=1
                                break
                            
                            #Cuando entre aquí, sera porque es diferente y no puede subir mas
                            else:
                                break
                        
                #Mover abajo lo que pueda 
                    if move:
                        if (moveToSimulate==DOWN):
                            boardToHandle[tomove][col].value = actualBox.value
                        else:
                            boardToHandle[col][tomove].value = actualBox.value
                        
                        actualBox.value = 0
                    move = False


        #self.showBoard(boardToHandle)

        if not (self.movementMaded(boardToHandle)): return -1

        return bloquesUnidosTemporal
       
    
    def bestMove(self) -> str :
        
        
        bloquesUnidosFinal = -1
        
        movimientoHaHacer = -1
        
        #UP
        print("UP") 
        unidos = self.simulateMovement(UP)
        if(unidos>bloquesUnidosFinal)   :
            bloquesUnidosFinal = unidos
            movimientoHaHacer = "up"
        
                                       
        print("LEFT")                                
        unidos = self.simulateMovement(LEFT)
        if(unidos>bloquesUnidosFinal)   :
            bloquesUnidosFinal = unidos
            movimientoHaHacer = "left"

        #DOWN


        print("DOWN")                                
        unidos = self.simulateMovement(DOWN)
        if(unidos>bloquesUnidosFinal)   :
            bloquesUnidosFinal = unidos
            movimientoHaHacer = "down"


        #RIGHT
        print("RIGHT")                                
        unidos = self.simulateMovement(RIGHT)
        if(unidos>bloquesUnidosFinal)   :
            bloquesUnidosFinal = unidos
            movimientoHaHacer = "right"
        
           

        print("MOV-> " ,movimientoHaHacer)

        return movimientoHaHacer



        
    def showBoard(self,boardd):

        board : str = ""
        for row in range(4):
            for col in range(4):
                board+= f"{boardd[row][col].value} | "
            board+="\n"
        
        print(board)