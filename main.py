from pynput.mouse import Listener

from Model import Board
from View import View
from Controller import Controller


import io
import pyscreenshot as ImageGrab
from PIL import Image
coord = []

def click(x,y,button,pressed):
    if pressed:
        x,y = x,y
        coord.append((x,y))

        if (len(coord) == 2):
            print("Coordenadas guardadas -> " , coord)
            return False # Detiene el listener
        

with Listener(on_click=click) as listener:
    listener.join()


left,top = coord[0]
right,bottom = coord[1]


sizeBlockWidth = (right - left) / 4
sizeBlockHeight = (bottom - top) / 4
SIZEBLOCK = max(sizeBlockHeight,sizeBlockWidth)


model = Board()

view = View(model,left,top,right,bottom,SIZEBLOCK)

controller = Controller(model,view)

controller.main_loop()
