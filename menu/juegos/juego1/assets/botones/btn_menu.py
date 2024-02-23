import pygame.font

background_color = (255, 255, 255)
button_color = (100, 100, 100)
text_color = (255, 255, 255)
class Btn_menu:
    def __init__(self, text, position, width, height,action):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, button_color, (self.position[0], self.position[1], self.width, self.height))
        font = pygame.font.SysFont(None, 36)
        text = font.render(self.text, True, text_color)
        text_rect = text.get_rect(center=(self.position[0] + self.width / 2, self.position[1] + self.height / 2))
        surface.blit(text, text_rect)
        
    def regresar_menu(self, mouse_pos):
        x, y = mouse_pos
        if self.position[0] < x < self.position[0] + self.width and self.position[1] < y < self.position[1] + self.height:
            return True
        return False