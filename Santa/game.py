import pygame
import random
import sys
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 120
SANTA_SPEED = 5
OBJECT_SPEED = 2
SPAWN_RATE = 30
WIN_SCORE = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Санта в космосе")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

IMAGE_FOLDER = "image"

santa_img = pygame.image.load(os.path.join(IMAGE_FOLDER, "santa.png")).convert_alpha()
santa_img = pygame.transform.scale(santa_img, (80, 60))

meteor_img = pygame.image.load(os.path.join(IMAGE_FOLDER, "meteor.png")).convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (40, 40))

fuel_img = pygame.image.load(os.path.join(IMAGE_FOLDER, "fuel.png")).convert_alpha()
fuel_img = pygame.transform.scale(fuel_img, (40, 30))

gift_img = pygame.image.load(os.path.join(IMAGE_FOLDER, "gift.png")).convert_alpha()
gift_img = pygame.transform.scale(gift_img, (40, 40))

space_bg = pygame.image.load(os.path.join(IMAGE_FOLDER, "space.jpg")).convert()
space_bg = pygame.transform.scale(space_bg, (WIDTH, HEIGHT))


class Santa:
    def __init__(self):
        self.width = 80
        self.height = 60
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = SANTA_SPEED
        self.fuel = 100
        self.score = 0
        self.image = santa_img

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed

    def update_fuel(self):
        self.fuel -= 0.1
        if self.fuel < 0:
            self.fuel = 0

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

        fuel_width = 200
        fuel_height = 20
        fuel_x = 10
        fuel_y = 10

        pygame.draw.rect(surface, WHITE, (fuel_x, fuel_y, fuel_width, fuel_height), 2)

        fill_width = int((self.fuel / 100) * fuel_width)
        fuel_color = GREEN if self.fuel > 50 else (255, 200, 0) if self.fuel > 25 else RED
        pygame.draw.rect(surface, fuel_color, (fuel_x + 2, fuel_y + 2, fill_width - 4, fuel_height - 4))

        fuel_text = font.render(f"Топливо: {int(self.fuel)}%", True, WHITE)
        surface.blit(fuel_text, (fuel_x + fuel_width + 10, fuel_y))

        score_text = font.render(f"Подарки: {self.score}/{WIN_SCORE}", True, WHITE)
        surface.blit(score_text, (WIDTH - 200, 10))

        if self.score < WIN_SCORE:
            win_width = 200
            win_height = 15
            win_x = WIDTH - win_width - 10
            win_y = 50

            pygame.draw.rect(surface, WHITE, (win_x, win_y, win_width, win_height), 1)
            progress_width = int((self.score / WIN_SCORE) * win_width)
            pygame.draw.rect(surface, GREEN, (win_x, win_y, progress_width, win_height))

            win_text = font.render(f"Цель: {WIN_SCORE}", True, WHITE)
            surface.blit(win_text, (win_x, win_y + 20))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class SpaceObject:
    def __init__(self, obj_type):
        self.type = obj_type
        self.size = random.randint(30, 50)
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.speed = random.randint(OBJECT_SPEED, OBJECT_SPEED + 2)

        if self.type == "gift":
            self.image = pygame.transform.scale(gift_img, (self.size, self.size))
        elif self.type == "fuel":
            fuel_height = int(self.size * 0.75)
            self.image = pygame.transform.scale(fuel_img, (self.size, fuel_height))
            self.size = (self.size, fuel_height)
        else:
            self.image = pygame.transform.scale(meteor_img, (self.size, self.size))

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        if isinstance(self.size, tuple):
            return pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        else:
            return pygame.Rect(self.x, self.y, self.size, self.size)

    def is_off_screen(self):
        if isinstance(self.size, tuple):
            return self.y > HEIGHT
        else:
            return self.y > HEIGHT


def show_game_over(screen, score, reason):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))

    if reason == "fuel":
        game_over_text = big_font.render("ЗАКОНЧИЛОСЬ ТОПЛИВО!", True, RED)
    elif reason == "meteor":
        game_over_text = big_font.render("СТОЛКНОВЕНИЕ С МЕТЕОРИТОМ!", True, RED)
    else:
        game_over_text = big_font.render("ИГРА ОКОНЧЕНА", True, RED)

    score_text = font.render(f"Собрано подарков: {score}/{WIN_SCORE}", True, WHITE)
    restart_text = font.render("Нажмите R для перезапуска или ESC для выхода", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 100))


def show_win_screen(screen, score):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 50, 0, 200))
    screen.blit(overlay, (0, 0))

    win_text = big_font.render("ПОБЕДА!", True, (255, 215, 0))
    congrats_text = font.render("Санта собрал все подарки!", True, WHITE)
    score_text = font.render(f"Собрано подарков: {score}/{WIN_SCORE}", True, WHITE)
    restart_text = font.render("Нажмите R для новой игры или ESC для выхода", True, WHITE)

    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(congrats_text, (WIDTH // 2 - congrats_text.get_width() // 2, HEIGHT // 2 - 20))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 20))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 100))


def show_start_screen():
    screen.blit(space_bg, (0, 0))

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    title = big_font.render("САНТА В КОСМОСЕ", True, RED)
    instruction1 = font.render("Управление: стрелки вверх, вниз, влево, вправо", True, WHITE)
    instruction2 = font.render(f"Соберите {WIN_SCORE} подарков для победы!", True, GREEN)
    instruction3 = font.render("Собирайте подарки и топливо (бензин)", True, WHITE)
    instruction4 = font.render("Избегайте метеоритов!", True, RED)
    instruction5 = font.render("Без топлива вы не можете лететь!", True, (255, 200, 0))
    instruction6 = font.render("Нажмите любую клавишу для начала игры", True, GREEN)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(instruction1, (WIDTH // 2 - instruction1.get_width() // 2, 200))
    screen.blit(instruction2, (WIDTH // 2 - instruction2.get_width() // 2, 250))
    screen.blit(instruction3, (WIDTH // 2 - instruction3.get_width() // 2, 300))
    screen.blit(instruction4, (WIDTH // 2 - instruction4.get_width() // 2, 350))
    screen.blit(instruction5, (WIDTH // 2 - instruction5.get_width() // 2, 400))
    screen.blit(instruction6, (WIDTH // 2 - instruction6.get_width() // 2, 480))

    screen.blit(gift_img, (WIDTH // 2 - 180, 520))
    gift_label = font.render("- подарок", True, WHITE)
    screen.blit(gift_label, (WIDTH // 2 - 130, 530))

    screen.blit(fuel_img, (WIDTH // 2, 520))
    fuel_label = font.render("- топливо", True, WHITE)
    screen.blit(fuel_label, (WIDTH // 2 + 50, 530))

    screen.blit(meteor_img, (WIDTH // 2 + 180, 520))
    meteor_label = font.render("- метеорит", True, WHITE)
    screen.blit(meteor_label, (WIDTH // 2 + 230, 530))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def main():
    santa = Santa()
    objects = []
    frame_count = 0
    game_over = False
    game_win = False
    game_over_reason = ""

    show_start_screen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if (game_over or game_win) and event.key == pygame.K_r:
                    santa = Santa()
                    objects = []
                    frame_count = 0
                    game_over = False
                    game_win = False
                    game_over_reason = ""

        if not game_over and not game_win:
            keys = pygame.key.get_pressed()
            santa.move(keys)
            santa.update_fuel()

            frame_count += 1
            if frame_count % SPAWN_RATE == 0:
                rand = random.random()
                if rand < 0.5:
                    obj_type = "gift"
                elif rand < 0.7:
                    obj_type = "fuel"
                else:
                    obj_type = "meteor"

                objects.append(SpaceObject(obj_type))

            for obj in objects[:]:
                obj.move()

                if santa.get_rect().colliderect(obj.get_rect()):
                    if obj.type == "gift":
                        santa.score += 1

                        if santa.score >= WIN_SCORE:
                            game_win = True

                    elif obj.type == "fuel":
                        santa.fuel = min(100, santa.fuel + 30)
                    elif obj.type == "meteor":
                        game_over = True
                        game_over_reason = "meteor"

                    objects.remove(obj)
                elif obj.is_off_screen():
                    objects.remove(obj)

            if santa.fuel <= 0:
                game_over = True
                game_over_reason = "fuel"

        screen.blit(space_bg, (0, 0))

        for obj in objects:
            obj.draw(screen)

        santa.draw(screen)

        if game_over:
            show_game_over(screen, santa.score, game_over_reason)
        elif game_win:
            show_win_screen(screen, santa.score)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()