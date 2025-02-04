''''''

from Model import Board
from View import View
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

import numpy as np


 
COLOR_DOS_RGB = [238, 228, 218]
COLOR_CUATRO_RGB = [237,223,200]
COLOR_OCHO_RGB = [242,177,121]
COLOR_16_RGB = [245,149,99]
COLOR_32_RGB = [246,124,95]
COLOR_64_RGB = [246,94,59]
COLOR_128_RGB = [237,206,114]
COLOR_256_RGB = [237,204,97]
COLOR_ZERO_RGB = [ 204,193,180]


def detectNumber(region) -> int:
    
    for x in range(10):
        for y in range(10):
            
            print(f"1 -> {region[x][y][0]} y {COLOR_ZERO_RGB[0]}")
            print(f"2-> {region[x][y][1]} y {COLOR_ZERO_RGB[1]}" )
            print(f"3 -> {region[x][y][2]} y {COLOR_ZERO_RGB[2]}")


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
      
        img = self.view.makeScreenshot()
        image_np = np.array(img)
       
        print(f"Tamagno bloque partido -> {self.view.SIZEBLOCK/2}")
        print(f"Tamagno bloque -> {self.view.SIZEBLOCK}")

        print(f"Bottom - {self.view.bottom}")
        print(f"right - {self.view.right}")

               
        self.createBoard(image_np,img)
        

                   
        self.view.showBoard()

        self.model.bestMove()
                
               
                
   
    def createBoard(self,image_np,img):
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

                # Guardar la subimagen de la región en un archivo
                if((row==2 and column==3) or (row==0 and column==0)):
                    subimage = img.crop((max(0, center_x - radio), max(0, center_y - radio),
                                                center_x + radio, center_y + radio))
                    subimage_path = f"region_row{row}_col{column}.png"
                    subimage.save(subimage_path)

                print(region[0][0])
                if(row==2 and column==3):
                    print("x")
                
                number = detectNumber(region)

                self.model.board[row][column].value = number

               
               # print(f"Fila {row} y columna {column} -> {image_np[row][column]}")

    def putAllNotJoined(self):  self.model.putAllNotJoined()