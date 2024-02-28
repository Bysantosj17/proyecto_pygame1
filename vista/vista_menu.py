import pygame, sys, os

from 

# Inicializar Pygame
pygame.init()
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

carpeta_actual = os.getcwd()
carpeta_raiz = os.path.dirname(carpeta_actual)
carpeta_proyecto = os.path.join(carpeta_raiz,"proyecto_pygame1")
carpeta_img = os.path.join(carpeta_proyecto, "imagenes")
carpeta_img_fondo = os.path.join(carpeta_img, "fondo")
print(carpeta_img_fondo)


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
        self.juego1_activado = True
        self.fondo = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_img_fondo,"fondo_1.png")).convert(), (screen_width, screen_height))
        self.btn_salir = Btn_salir("Salir", ((screen_width//3.6), (screen_height//1.30)), 600,60)
        #self.btn_juego1 = Btn_juego_1("Telefono sin numeros",  ((screen_width//3.60), (screen_height//1.50)), 290,60, Telefono_sin_num.corre_juego1)
        #self.btn_juego2 = Btn_juego_1("Iguala la imagen",  ((screen_width// 1.98), (screen_height//1.50)), 290,60, Iguala_imagen.corre_juego2)