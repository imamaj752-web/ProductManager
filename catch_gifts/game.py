from classes.text import Text
from classes.button import Button
from classes.bag import Bag
from classes.gift import Gift

import pygame
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
clock = pygame.time.Clock()


'''Музика та звуки'''
# завантажуємо музику, встановлюємо гучність, запускаємо
pygame.mixer.music.load("sounds/bg.mp3")
pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1)

# завантажуємо звуки
sound_start_game = pygame.mixer.Sound('sounds/start_game.mp3')
sound_start_game.set_volume(0.3)

'''Фон'''
bg_image = pygame.image.load('images/bg.jpg')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

'''Ігрові лічильники'''
catch_gifts = 0

'''Текст'''
name_game = Text('Catch gift', color=(0, 0, 150), font_size=150)
score = Text(f'Score: {catch_gifts}', color=(255, 255, 255), font_size=30)
game_over = Text('Game over', color=(255, 255, 255), font_size=150)

'''Кнопки'''
start_button = Button('Play', color=(0, 200, 0), size=(400, 100))
exit_button = Button('Exit', color=(200, 0, 0), size=(400, 100))
try_again = Button('Try again', color=(0, 200, 0), size=(400, 100))

'''Ігрові об'єкти'''
bag = Bag(pos=(WIDTH//2, HEIGHT - 150))

# група для спрайтів
gifts = pygame.sprite.Group()

for _ in range(5):
    gift = Gift()
    gifts.add(gift) # додаємо спрайт у групу


# поточний етап гри
MODE_GAME = 'menu'

run_game = True
while run_game:
    clock.tick(FPS)
    screen.blit(bg_image, (0, 0))

    # якщо етап гри МЕНЮ
    if MODE_GAME == 'menu':
        # відмальовуємо текст
        name_game.show(screen, (WIDTH//2, 200))

        # відмальовуємо кнопку
        start_button.show(screen, (WIDTH//2, 400))
        exit_button.show(screen, (WIDTH//2, 600))

    # якщо етап гри ГРА
    elif MODE_GAME == 'game':
        score.show(screen, (WIDTH // 2, 50))

        screen.blit(bag.image, bag.rect)
        bag.update()

        # відмальовуємо групу спрайтів
        gifts.draw(screen)

        # викликається update для кожного подарунку
        gifts.update()

        # перевіряємо колізію подарунків з мішком
        for gift in gifts:
            if gift.is_collision(bag):
                gift.reset()

                # змінюємо кількість подарунків
                if gift.type == 'good':
                    catch_gifts += 1
                else:
                    catch_gifts -= 1

                score = Text(f'Score: {catch_gifts}', color=(255, 255, 255), font_size=30)

                # перехід до фінішу
                if catch_gifts >= 10 or catch_gifts <= -2:
                    MODE_GAME = 'finish'

    elif MODE_GAME == 'finish':
        result_game = Text(f'{"Win" if catch_gifts > 0 else "Lose"}', color=(0, 0, 150), font_size=100)
        result_game.show(screen, (WIDTH // 2, 350))

        game_over.show(screen, (WIDTH // 2, 200))
        try_again.show(screen, (WIDTH // 2, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # клік по кнопці старт та try again
            if (start_button.is_clicked() and MODE_GAME == 'menu') or (try_again.is_clicked() and MODE_GAME == 'finish'):

                # змінюємо етап гри
                MODE_GAME = 'game'

                # обнуляємо бали
                catch_gifts = 0
                score = Text(f'Score: {catch_gifts}', color=(255, 255, 255), font_size=30)

                # запускаємо програвання звуку
                sound_start_game.play()

            elif exit_button.is_clicked() and MODE_GAME == 'menu':
                run_game = False


    pygame.display.flip()