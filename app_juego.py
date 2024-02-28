import pygame

pygame.init()
#Menu
from vista.vista_menu import *
from controlador.controlador_vista_menu import *

if __name__ == "__main__":
    vista_menu = Menu_game()
    controlador_vista_menu = corre_menu(vista_menu)
    