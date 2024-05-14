import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Скорость игрока
PLAYER_SPEED = 5

# Скорость дополнительного спрайта
BONUS_SPEED = 3

# Количество очков за сбор дополнительного спрайта
BONUS_POINTS = 10

# Количество очков, снимаемое при столкновении с шипами
SPIKE_POINTS = 5

# Настройки меню
MENU_OPTIONS = ["Start", "Settings", "Exit"]
MENU_OPTION_FONT = pygame.font.SysFont("Arial", 30)
MENU_OPTION_SELECTED_COLOR = GREEN
MENU_OPTION_UNSELECTED_COLOR = WHITE

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Спрайты
player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill(BLUE)
player.rect = player.image.get_rect()
player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

bonus = pygame.sprite.Sprite()
bonus.image = pygame.Surface((20, 20))
bonus.image.fill(GREEN)
bonus.rect = bonus.image.get_rect()
bonus.rect.x = random.randrange(SCREEN_WIDTH - bonus.rect.width)
bonus.rect.y = random.randrange(SCREEN_HEIGHT - bonus.rect.height)

spikes = pygame.sprite.Group()
for i in range(10):
    spike = pygame.sprite.Sprite()
    spike.image = pygame.Surface((20, 20))
    spike.image.fill(RED)
    spike.rect = spike.image.get_rect()
    spike.rect.x = random.randrange(SCREEN_WIDTH - spike.rect.width)
    spike.rect.y = random.randrange(SCREEN_HEIGHT - spike.rect.height)
    spikes.add(spike)

# Очки
score = 0
score_font = pygame.font.SysFont("Arial", 30)

# Музыка
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)

# Звуки
bonus_sound = pygame.mixer.Sound("bonus.wav")
spike_sound = pygame.mixer.Sound("spike.wav")

# Флаги
running = True
in_menu = True
music_playing = True

# Меню
menu_option_selected = 0

# Цикл игры
while running:
    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if in_menu:
                if event.key == pygame.K_DOWN:
                    menu_option_selected += 1
                    if menu_option_selected > len(MENU_OPTIONS) - 1:
                        menu_option_selected = 0
                elif event.key == pygame.K_UP:
                    menu_option_selected -= 1
                    if menu_option_selected < 0:
                        menu_option_selected = len(MENU_OPTIONS) - 1
                elif event.key == pygame.K_RETURN:
                    if MENU_OPTIONS[menu_option_selected] == "Start":
                        in_menu = False
                    elif MENU_OPTIONS[menu_option_selected] == "Settings":
                        # Настройки
                        pass
                    elif MENU_OPTIONS[menu_option_selected] == "Exit":
                        running = False
            else:
                if event.key == pygame.K_ESCAPE:
                    in_menu = True
                elif event.key == pygame.K_SPACE:
                    music_playing = not music_playing
                    if music_playing:
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.pause()
        elif event.type == pygame.KEYUP:
            pass

    # Обновление
    if not in_menu:
        # Перемещение игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            player.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player.rect.y += PLAYER_SPEED

        # Проверка границ экрана
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
        if player.rect.top < 0:
            player.rect.top = 0
        if player.rect.bottom > SCREEN_HEIGHT:
            player.rect.bottom = SCREEN_HEIGHT

        # Столкновения
        if pygame.sprite.spritecollideany(player, bonus):
            bonus.rect.x = random.randrange(SCREEN_WIDTH - bonus.rect.width)
            bonus.rect.y = random.randrange(SCREEN_HEIGHT - bonus.rect.height)
            score += BONUS_POINTS
            bonus_sound.play()
        if pygame.sprite.spritecollideany(player, spikes):
            for i in range(5):
                particle = pygame.sprite.Sprite()
                particle.image = pygame.Surface((10, 10))
                particle.image.fill(BLUE)
                particle.rect = particle.image.get_rect()
                particle.rect.center = player.rect.center
                spike_sound.play()
            score -= SPIKE_POINTS

    # Рендеринг
    screen.fill(BLACK)
    if in_menu:
        # Рендеринг меню
        for i, option in enumerate(MENU_OPTIONS):
            if i == menu_option_selected:
                color = MENU_OPTION_SELECTED_COLOR
            else:
                color = MENU_OPTION_UNSELECTED_COLOR
            text_surface = MENU_OPTION_FONT.render(option, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (SCREEN_WIDTH / 2, (i + 1) * 100)
            screen.blit(text_surface, text_rect)
    else:
        # Рендеринг игры
        screen.blit(player.image, player.rect)
        screen.blit(bonus.image, bonus.rect)
        for spike in spikes:
            screen.blit(spike.image, spike.rect)

        # Рендеринг очков
        score_text = score_font.render(str(score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        screen.blit(score_text, score_rect)

    # Отображение экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)

# Выход из Pygame
pygame.quit()





#cсылка на мой гит хаб https://github.com/faruh121/python-kod-bud