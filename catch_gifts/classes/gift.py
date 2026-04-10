import random
import pygame


class Gift(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.set_type()

        self.rect = self.image.get_rect()
        self.reset()

    def set_type(self):
        self.type = random.choice(['good', 'bad'])

        self.image = pygame.image.load(f'images/{self.type}_gift.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))


    def reset(self):
        self.rect.x = random.randint(0, 1200)
        self.rect.y = 0

        self.speed = random.randint(1, 10)

        self.set_type()

    def is_collision(self, _object):
        # colliderect перевіряє колізію (пересічення) прямокутників
        return self.rect.colliderect(_object.rect)

    def update(self):
        # постійно рухається униз
        self.rect.y += self.speed

        if self.rect.y >= 900:
            self.reset()