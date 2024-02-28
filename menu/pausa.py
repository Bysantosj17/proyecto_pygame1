import pygame, sys

# Inicializar Pygame
pygame.init()
#colors
#BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
AZUL_CIELO = (92, 241, 254 )
BLACK = (0, 0, 0)

class VentanaPausa:
    def __init__(self,v_pausa):
        self.v_pausa = v_pausa
        self.dimensiones_v_pausa = v_pausa.get_size()
        self.fondo = pygame.Surface.Surface(self.dimensiones_v_pausa)
        self.fondo.set_alpha(128)
        self.fondo.fill(BLACK)
        
        self.font = pygame.font.SysFont(None, 36)
        self.texto_pausa = self.font.render("Pausa", True, WHITE)
        self.rect_texto_pausa = self.texto_pausa.get_rect(center = (self.dimensiones_v_pausa[0] // 2, 100))
        
        self.texto_continuar = self.font.render("Presiona 'P' para continuar", True, WHITE)
        self.rect_texto_continuar = self.texto_continuar.get_rect(center=(self.dimensiones_v_pausa[0] // 2, 200))
        
    def mostrar(self):
        self.ventana.blit(self.fondo, (0,0))
        self.ventana.blit(self.texto_pausa, self.rect_texto_pausa)
        self.ventana.blit(self.texto_continuar, self.rect_texto_continuar)
        pygame.display.flip()