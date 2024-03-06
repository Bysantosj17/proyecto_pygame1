import pygame,sys, os

pygame.init()

from proyecto.menu.juegos.juego_1.assets.botones.btn_menu import *




#colors
#BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
AZUL_CIELO = (92, 241, 254 )

'''carpeta_proyecto = os.path.dirname(__file__)
carpeta_img_menu = os.path.join(carpeta_proyecto, "img_menu")'''


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
        self.ejecutar = True
        self.btn_menu = Btn_menu("Pausa", (((screen_width // 1.2)), ((screen_height // 12)-50)), 180,50)
        
    def corre_juego_1(self):
        while self.ejecutar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ejecutar = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn_menu.ir_menu(pygame.mouse.get_pos()):
                        self.ejecutar = False
        
            self.juego_1.fill(self.color_font)
            self.btn_menu.draw(self.juego_1)
            
            
            pygame.display.flip()
        pygame.quit()
        sys.exit()
            
