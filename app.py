import pygame

from proyecto.menu.menu import *

def main():
    pygame.init()
    menu = Menu_game()
    menu.corre_menu()

if __name__ == "__main__":
    main()