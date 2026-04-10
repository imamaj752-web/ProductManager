import pygame


# клас Sprite дозволяє описувати ігрові об'єкти
class Bag(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # обов'язкові атрибути (image, rect)
        self.image = pygame.image.load('images/bag.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (270, 250))

        self.rect = self.image.get_rect()
        self.rect.center = pos

        # індивідуальні атрибути
        self.step = 10

    # update - описує поведінку об'єкту
    def update(self):
        # зчитуємо клавіши
        keys = pygame.key.get_pressed()

        # стрілка вліво та вправо
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # обмежуємо рух вліво (в межах екрану)
            if self.rect.left > 0:
                self.rect.x -= self.step

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # обмежуємо рух вправо (в межах екрану)
            if self.rect.right < 1200:
                self.rect.x += self.step