import pygame,sys


def corre_menu(self):
    while True:
        self.main_menu.blit(self.fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #self.juego_1.fill(self.color_font)
        #self.btn_menu.draw(self.juego_1)
        
        pygame.display.flip()
        
