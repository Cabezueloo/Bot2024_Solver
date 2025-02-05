import numpy as np
import array as arr
import copy
from ollama import chat
from ollama import ChatResponse


UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4
moviments = dict()
moviments[UP] = "up"
moviments[LEFT] = "left"
moviments[DOWN] = "down"
moviments[RIGHT] = "right"

POSSIBLE_MOVEMENTS : list = [UP,RIGHT,DOWN,LEFT]

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

    

    def simulateMovement(self,moveToSimulate,boardToHandle,dictionaryMergedBlocks : dict = dict(), exit : int= 0,bloquesUnidosTemporal : int = 0 ) -> int:
        
                       
        tomove= -1
        move = False
        movementMaded = False
        #UP-LEFT merge
        if(moveToSimulate==UP or moveToSimulate == LEFT):
            for col in range(4):

                for row in range(4):

                    actualBox = boardToHandle[row][col] if moveToSimulate==UP else boardToHandle[col][row]
                   

                    if (row-1>=0 and actualBox.value != 0):

                        for y in range(0,row):

                            simultadeBox = boardToHandle[row-y-1][col] if (moveToSimulate==UP) else boardToHandle[col][row-y-1]

                            #Si arriba es 0, no hara nada ya que podrá ver mas alla de ese
                            if (simultadeBox.value == 0):
                                move  = True
                                tomove = row-y-1
                                
                                pass

                            #Si la de arriba es igual, lo sumara arriba
                            elif(simultadeBox.value == actualBox.value and not simultadeBox.joined):
                               
                                self.mergeValues(simultadeBox,actualBox)
                                bloquesUnidosTemporal+=1
                                break

                            #Cuando entre aquí, sera porque es diferente y no puede subir mas
                            else:
                                break

                    if(move):
                        movementMaded = True
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
                   
                    actualBox = boardToHandle[row][col] if (moveToSimulate==DOWN) else boardToHandle[col][row]
                    
                    #print("Actual value -> ",actualBox.value)

                    if (row+1<=4 and actualBox.value != 0):
                        cont = 0
                        for y in range(row,3):
                            
                            cont+=1
                            simultadeBox = boardToHandle[row+cont][col] if (moveToSimulate==DOWN) else boardToHandle[col][row+cont]
                            
                            #print("Simuleted value -> ",simultadeBox.value)

                            #Si abajo es 0, no hara nada ya que podrá ver mas alla de ese
                            if (simultadeBox.value == 0):
                                move  = True
                                tomove = row+cont
                                
                                pass

                            #Si la de abajo es igual, lo sumara abajo
                            elif(simultadeBox.value == actualBox.value and not simultadeBox.joined):
                                
                                self.mergeValues(simultadeBox,actualBox)
                                bloquesUnidosTemporal+=1
                                break
                            
                            #Cuando entre aquí, sera porque es diferente y no puede subir mas
                            else:
                                break
                        
                #Mover abajo lo que pueda 
                    if move:
                        movementMaded = True
                        if (moveToSimulate==DOWN):
                            boardToHandle[tomove][col].value = actualBox.value
                        else:
                            boardToHandle[col][tomove].value = actualBox.value
                        
                        actualBox.value = 0
                    move = False

        #print(moveToSimulate)
        #self.showBoard(boardToHandle)

        #Cuando sea 1, no hara mas posiblidades de recursividad y retornara
        if not exit == 1 :
            if not (movementMaded) : 
                print(f"No ha hecho movimientos -> {moveToSimulate}")
                return -1
            
            bloquesRetornoFinal = bloquesUnidosTemporal   
            for movement in POSSIBLE_MOVEMENTS:
                
                bloquesRetornoTemp = self.simulateMovement(movement, copy.deepcopy(boardToHandle), copy.deepcopy(dictionaryMergedBlocks),exit = exit+1 )
                
                #print(f"Bloques unidos temporal {bloquesUnidosTemporal}")
                #print(f"Bloques retorno temp {bloquesRetornoTemp}")
                #print(f"Bloques retorno final {bloquesRetornoFinal}")

                if(bloquesRetornoTemp+bloquesUnidosTemporal>bloquesRetornoFinal):
                    bloquesRetornoFinal = bloquesRetornoTemp+bloquesUnidosTemporal
            print(f"Bloques retorno final -> {bloquesRetornoFinal}" )
            #Retorno final
            return bloquesRetornoFinal

        #De recurvidad
        return bloquesUnidosTemporal
    
    def mergeValues(self, simultadeBox,actualBox):
        actualBox.value = 0
        simultadeBox.value +=simultadeBox.value
        simultadeBox.joined = True
        move = False
        movementMaded = True
        
        
    
    def bestMove(self,IA:bool) -> str :
        
        if not IA:
            bloquesUnidosFinal = -1
            movimientoHaHacer = -1
            
            
            
            
            for key,value in moviments.items():
                unidos = self.simulateMovement(key, copy.deepcopy(self.board))
                if(unidos>bloquesUnidosFinal):
                    bloquesUnidosFinal = unidos
                    movimientoHaHacer = value

        # TODO IA turn    
        else:
            print(self.returnBoard())
            response : ChatResponse = chat(model="llama3.2",messages=[
                {
                    'role' : 'user',
                    'content':  f'I need you to tell me what move to do in the game 2048, you can only answer (right, left, up, down).  Based on the move to make. Remember, the answer must be one word only,lowercase and without dots\nHere is the current game board\n{self.returnBoard()}'
                    
                }
            ])
            movimientoHaHacer =(response.message.content)

        

        return movimientoHaHacer



    def returnBoard(self) -> str:
        answ : str = ""
        for row in range(4):
            for col in range(4):
                answ+= f"{self.board[row][col].value} | "
            answ+="\n"
        
        return answ


    def showBoard(self,boardd):

        board : str = ""
        for row in range(4):
            for col in range(4):
                board+= f"{boardd[row][col].value} | "
            board+="\n"
        
        print(board)