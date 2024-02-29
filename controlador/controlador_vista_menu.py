import pygame,sys

from botones.btn_juegos import *

from controlador.controlador_vista_juego1 import *
from controlador.controlador_vista_juego2 import *
from controlador.controlador_vista_menu import *

from vista.vista_Telefono_s_num import *
from vista.vista_menu import *
from vista.vista_igual_imagen import *

ejecutando = True
def corre_menu(self):
    while True:
        self.main_menu.blit(self.fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn_salir.is_clicked(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    if self.btn_juego1.Iniciar_juego(pygame.mouse.get_pos()):
                            vista_Telefono_s_num = Telefono_sin_num()
                            controlador_vista_juego_1 = corre_Tel_s_num(vista_Telefono_s_num)
                    '''if self.btn_juego2.Iniciar_juego(pygame.mouse.get_pos()):
                            vista_igual_imagen = Igual_a_img()
                            controlador_vista_juego2 = corre_juego2(vista_igual_imagen)'''
                        
        self.btn_salir.draw(self.main_menu)
        self.btn_juego1.draw(self.main_menu)
        self.btn_juego2.draw(self.main_menu)

        
        pygame.display.flip()
    
        pygame.quit()