import pygame


class Text:
    def __init__(self, text, color, font_name='Impact', font_size=100):
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect()

    def show(self, screen, pos: tuple[int, int]):
        self.rect.center = pos
        screen.blit(self.text, self.rect)
