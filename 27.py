import pygame
import random

# Инициализация
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -6
PIPE_SPEED = 4
PIPE_GAP = 150

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEON_BLUE = (0, 255, 255)
NEON_GREEN = (57, 255, 20)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Neon Fly")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

class Bird:
    def __init__(self):
        self.y = SCREEN_HEIGHT // 2
        self.x = 50
        self.vel = 0
        self.width = 30
        self.height = 30

    def flap(self):
        self.vel = FLAP_STRENGTH

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, NEON_BLUE, self.rect, border_radius=7)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.passed = False
        self.top_rect = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, 50, SCREEN_HEIGHT)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, NEON_GREEN, self.top_rect)
        pygame.draw.rect(screen, NEON_GREEN, self.bottom_rect)

def main():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + 100)]
    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Обновление птицы
        bird.update()

        # Логика труб
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe(SCREEN_WIDTH))

        for pipe in pipes:
            pipe.update()
            pipe.draw()

            # Проверка столкновений
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                running = False

            # Подсчет очков
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                score += 1

        # Удаление лишних труб
        pipes = [p for p in pipes if p.x > -50]

        # Проверка границ экрана
        if bird.y > SCREEN_HEIGHT or bird.y < 0:
            running = False

        bird.draw()

        # Вывод счета
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()