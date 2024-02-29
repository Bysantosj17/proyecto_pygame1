import pygame,sys

pygame.init()

def corre_juego2(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        self.juego_2.fill(self.color_font)
        #self.btn_menu.draw(self.juego_1)
        
        pygame.display.flip()