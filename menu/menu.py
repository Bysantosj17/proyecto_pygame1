import pygame, sys,os
import pygame.font

from menu.assets.botones.btn_salir import *
from menu.assets.botones.btn_juego1 import *
from menu.juegos.juego1.juego1 import *
from menu.juegos.juego2.juego2 import *

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

class menu_game:
    def __init__(self):
        pygame.init()
        self.main_menu = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.color_font = (AZUL_CIELO)
        self.juego1_activado = True
        self.btn_salir = Button("Salir", ((screen_width//2.9), (screen_height//1.3)), 600,60)
        self.btn_juego1 = Btn_juego_1("Telefono sin numeros",  ((screen_width//2.90), (screen_height//1.45)), 280,60, Telefono_sin_num.corre_juego1)
        self.btn_juego2 = Btn_juego_1("Juego_2",  ((screen_width//2), (screen_height//3)), 280,60, juego2.corre_juego2)
        
        
    def corre_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn_salir.is_clicked(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    if self.btn_juego1.Iniciar_juego_1(pygame.mouse.get_pos()):
                            a = Telefono_sin_num()
                            a.corre_juego1()
                    if self.btn_juego2.Iniciar_juego_1(pygame.mouse.get_pos()):
                            a = juego2()
                            a.corre_juego2()
            
            self.main_menu.fill(self.color_font)
            self.btn_salir.draw(self.main_menu)
            self.btn_juego1.draw(self.main_menu)
            self.btn_juego2.draw(self.main_menu)

                

            pygame.display.flip()
            