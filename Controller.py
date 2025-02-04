''''''

from Model import Board
from View import View
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import keyboard 
import time
import numpy as np
import pyautogui


 
COLOR_DOS_RGB = [239, 228, 219]
COLOR_CUATRO_RGB = [238,223,202]
COLOR_OCHO_RGB = [246,176,126]
COLOR_16_RGB = [249,149,105]
COLOR_32_RGB = [251,125,100]
COLOR_64_RGB = [251,95,68]
COLOR_128_RGB = [240,205,122]
COLOR_256_RGB = [240,202,107]
COLOR_ZERO_RGB = [ 205,193,181]


def detectNumber(region) -> int:
    
    for x in range(10):
        for y in range(10):
            
           # print(f"1 -> {region[x][y][0]}")
            #print(f"2-> {region[x][y][1]}" )
            #print(f"3 -> {region[x][y][2]}")


            if region[x][y][0]==COLOR_ZERO_RGB[0] and region[x][y][1]==COLOR_ZERO_RGB[1] and (region[x][y][2]==COLOR_ZERO_RGB[2] or region[x][y][2]==178):
                return 0
            if region[x][y][0]==COLOR_DOS_RGB[0] and region[x][y][1]==COLOR_DOS_RGB[1] and region[x][y][2]==COLOR_DOS_RGB[2]:
                return 2
            if region[x][y][0]==COLOR_CUATRO_RGB[0] and region[x][y][1]==COLOR_CUATRO_RGB[1] and region[x][y][2]==COLOR_CUATRO_RGB[2]:
                return 4
            if region[x][y][0]==COLOR_OCHO_RGB[0] and region[x][y][1]==COLOR_OCHO_RGB[1] and region[x][y][2]==COLOR_OCHO_RGB[2]:
                return 8
            if region[x][y][0]==COLOR_16_RGB[0] and region[x][y][1]==COLOR_16_RGB[1] and region[x][y][2]==COLOR_16_RGB[2]:
                return 16 
            if region[x][y][0]==COLOR_32_RGB[0] and region[x][y][1]==COLOR_32_RGB[1] and region[x][y][2]==COLOR_32_RGB[2]:
                return 32 
            
            
            if region[x][y][0]==COLOR_64_RGB[0] and region[x][y][1]==COLOR_64_RGB[1] and region[x][y][2]==COLOR_64_RGB[2]:                
                return 64
            if region[x][y][0]==COLOR_128_RGB[0] and region[x][y][1]==COLOR_128_RGB[1] and region[x][y][2]==COLOR_128_RGB[2]:                
                return 128
            if region[x][y][0]==COLOR_256_RGB[0] and region[x][y][1]==COLOR_256_RGB[1] and region[x][y][2]==COLOR_256_RGB[2]:                
                return 256



            
    return -1

class Controller:
    
    def __init__(self,model: Board, view:View):
        self.model : Board= model
        self.view : View= view

    


    def main_loop(self):
        
        for x in range(2000):
            t = time.time()
            img = self.view.makeScreenshot()
            image_np = np.array(img)
            
                    
            self.createBoard(image_np,img)

            move = self.model.bestMove()
            
            print("--------------------")
            
            print("ORIGINAl")                                
            self.view.showBoard()
            
            pyautogui.press(move)
            print(f"Tiempo en saber la mejor pulsación -> {time.time() - t}")
            

              
    def createBoard(self,image_np,img):
        self.putAllNotJoined()

        for row in range(4):

            for column in range(4):
                row_pixel = column*self.view.SIZEBLOCK
               # Calcular el centro de cada celda
                center_x, center_y = (column * self.view.SIZEBLOCK + 0.5 * self.view.SIZEBLOCK, \
                row * self.view.SIZEBLOCK + 0.50 * self.view.SIZEBLOCK)
                center_x = int(center_x)
                center_y = int(center_y)

                # Definir un radio alrededor del centro (opcional, dependiendo de cuántos píxeles quieras inspeccionar)
                # Puedes ajustar este valor
                #radio = 10 #50%
                radio = 40 #65% zoom +-
                
                # Obtener los píxeles dentro del radio alrededor del centro
                region = image_np[max(0, center_y - radio): center_y + radio, max(0, center_x - radio): center_x + radio]

                                    
                number = detectNumber(region)

                self.model.board[row][column].value = number

               
               # print(f"Fila {row} y columna {column} -> {image_np[row][column]}")

    def putAllNotJoined(self):  self.model.putAllNotJoined()