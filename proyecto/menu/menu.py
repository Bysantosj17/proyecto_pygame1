import pygame, sys

pygame.init()

from proyecto.menu.assets.botones.btn_salir import *
from proyecto.menu.assets.botones.btn_juegos import *
from proyecto.menu.juegos.juego_1.juego1 import Telefono_sin_num


#colors
#BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
AZUL_CIELO = (92, 241, 254 )
background_color = (255, 255, 255)
button_color = (100, 100, 100)
text_color = (255, 255, 255)

'''carpeta_actual = os.getcwd()
carpeta_raiz = os.path.dirname(carpeta_actual)
carpeta_proyecto = os.path.join(carpeta_raiz,"proyecto_pygame1")
carpeta_img = os.path.join(carpeta_proyecto, "imagenes")
carpeta_img_fondo = os.path.join(carpeta_img, "fondo")
print(carpeta_img_fondo)'''

# Obtener las dimensiones de la pantalla del dispositivo
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

class Menu_game:
    def __init__(self):
        pygame.init()
        self.main_menu = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.color_font = (AZUL_CIELO)
        pygame.display.set_caption("Menu principal")
        self.btn_salir = Btn_salir("Salir", (((screen_width//3.6)+125), (screen_height//1.30)), 600,60)
        self.btn_juego1 = Btn_juegos("Telefono sin numeros",  ((screen_width//3.60), (screen_height//1.50)), 290,60)

    def corre_menu(self):
        ejecutar = True
        while ejecutar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ejecutar = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn_salir.salir(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    if self.btn_juego1.Iniciar_juego(pygame.mouse.get_pos()):
                        a = Telefono_sin_num()
                        a.corre_juego_1()


            self.main_menu.fill(self.color_font)
            self.btn_salir.draw(self.main_menu)
            self.btn_juego1.draw(self.main_menu)


            pygame.display.flip()
        pygame.quit()
        sys.exit()
