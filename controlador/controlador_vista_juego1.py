
import pygame,sys

from vista.vista_Telefono_s_num import *
from vista.vista_menu import*
from app_juego import *

from botones.btn_menu import *

pygame.init()

def corre_Tel_s_num(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
        self.juego_1.fill(self.color_font)
        self.btn_menu.draw(self.juego_1)
        
        pygame.display.flip()
        