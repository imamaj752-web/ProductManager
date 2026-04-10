import pygame
from .text import Text


class Button:
    def __init__(self, text, color, size: tuple[int, int]):
        self.color_border = (255, 255, 255)
        self.color_text = (0, 0, 0)
        self.color_bg = color

        self.rect = pygame.Rect((0, 0), size)
        self.text = Text(text, self.color_text, font_size=70)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def show(self, screen, pos: tuple[int, int]):
        self.rect.center = pos

        # border_radius - скруглення кутів
        pygame.draw.rect(screen, self.color_bg, self.rect, border_radius=50)

        # width - товщина обводки (прямоктник без заливки)
        pygame.draw.rect(screen, self.color_border, self.rect, border_radius=50, width=5)

        self.text.show(screen, self.rect.center)