import pygame
import random
import sys

pygame.init()

# Настройки
WIDTH, HEIGHT = 600, 800
FPS = 60
PLAYER_SIZE = 50
BLOCK_SIZE = 50
BLOCK_SPEED = 15
SPAWN_DELAY = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Блок Баст")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

# Игрок
player = pygame.Rect(WIDTH // 2, HEIGHT - 100, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 7

# Блоки
blocks = []
spawn_timer = 0
score = 0

def draw_text(text, x, y):
    render = font.render(text, True, (255, 255, 255))
    screen.blit(render, (x, y))

running = True
while running:
    clock.tick(FPS)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Спавн блоков
    spawn_timer += 1
    if spawn_timer >= SPAWN_DELAY:
        block_x = random.randint(0, WIDTH - BLOCK_SIZE)
        blocks.append(pygame.Rect(block_x, 0, BLOCK_SIZE, BLOCK_SIZE))
        spawn_timer = 0

    # Движение блоков
    for block in blocks[:]:
        block.y += BLOCK_SPEED
        if block.colliderect(player):
            print("Игра окончена! Счёт:", score)
            pygame.quit()
            sys.exit()
        if block.top > HEIGHT:
            blocks.remove(block)
            score += 1

    # Рисуем игрока
    pygame.draw.rect(screen, (0, 100, 255), player)

    # Рисуем блоки
    for block in blocks:
        pygame.draw.rect(screen, (255, 50, 50), block)

    draw_text(f"Счёт: {score}", 10, 10)

    pygame.display.flip()

pygame.quit()