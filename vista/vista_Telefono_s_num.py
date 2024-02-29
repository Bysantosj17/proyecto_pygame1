import pygame,os,sys

from botones.btn_menu import *

# Inicializar Pygame
pygame.init()
#colors
#BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
AZUL_CIELO = (92, 241, 254 )

carpeta_proyecto = os.path.dirname(__file__)
carpeta_img_menu = os.path.join(carpeta_proyecto, "img_menu")


# Obtener las dimensiones de la pantalla del dispositivo
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

class Telefono_sin_num:
    def __init__(self):
        pygame.init()
        self.juego_1 = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.color_font = (BLUE)
        pygame.display.set_caption("Telefono descompuesto")
        self.btn_menu = Btn_menu("Menu", ((screen_width // 2), (screen_height // 2)), 600,60)