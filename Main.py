import pygame
import os
import Player
import Button
import Level

pygame.init()

SIZESCREEN = WIDTH, HEIGHT = 1200, 1000
screen = pygame.display.set_mode(SIZESCREEN)
clock = pygame.time.Clock()
path = os.path.join(os.getcwd(), 'images')
path2 = os.path.join(os.getcwd(), 'music')
file_names = os.listdir(path)
BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()
file_names.remove('background.png')
IMAGES = {}
for file_name in file_names:
    image_name = file_name[:-4].upper()
    IMAGES[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha()
obstacles = [
            pygame.Rect(262, 616, 190, 12),
            pygame.Rect(442, 626, 10, 40),
            pygame.Rect(128, 615, 10, 235),
            pygame.Rect(39, 733, 90, 115),
            pygame.Rect(140, 840, 140, 10),
            pygame.Rect(283, 787, 170, 60),
            pygame.Rect(91, 79, 10, 120),
            pygame.Rect(102, 78, 180, 10),
            pygame.Rect(90, 200, 40, 10),
            pygame.Rect(284, 78, 10, 130),
            pygame.Rect(242, 200, 40, 10),
            pygame.Rect(437, 127, 80, 5),
            pygame.Rect(518, 137, 60, 5),
            pygame.Rect(570, 144, 50, 5),
            pygame.Rect(620, 150, 50, 5),
            pygame.Rect(670, 155, 50, 5),
            pygame.Rect(592, 244, 65, 70),
            pygame.Rect(560, 777, 80, 75),
            pygame.Rect(1000, 273, 50, 5),
            pygame.Rect(1004, 282, 5, 100),
            pygame.Rect(1005, 383, 20, 5),
            pygame.Rect(1130, 380, 25, 5),
            pygame.Rect(956, 115, 80, 5),
            pygame.Rect(960, 39, 5, 70),
            pygame.Rect(890, 697, 80, 70),
]

player = Player.Player(IMAGES['PLAYER'], 300, 300, obstacles)
points_font = pygame.font.Font(None, 36)
start = Button.Button(IMAGES['START'], WIDTH // 2 - 130 , HEIGHT // 2 - 100)
end = Button.Button(IMAGES['EXIT'], WIDTH // 2 - 130, HEIGHT // 2 + 100)
game_over = IMAGES['OVER']
game_over_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
window_open = True
active_game = False
current_level = Level.Level_1(player, IMAGES)
lose = pygame.mixer.Sound(os.path.join(path2, 'game_fail.ogg'))
shoot = pygame.mixer.Sound(os.path.join(path2, 'shoot.ogg'))
music = pygame.mixer.Sound(os.path.join(path2, 'music.ogg'))

while window_open:

    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active_game = False
                start.set_active(True)
                end.set_active(True)
                current_level.music.stop()

        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start.rect.collidepoint(pygame.mouse.get_pos()) and start.active:

                active_game = True
                start.set_active(False)
                end.set_active(False)
                pygame.time.delay(200)
                current_level = Level.Level_1(player, IMAGES)
                current_level.reset()
                current_level.music.stop()
            if end.rect.collidepoint(pygame.mouse.get_pos()) and end.active:
                window_open = False

                pygame.time.delay(200)

    if active_game:

        key_pressed = pygame.key.get_pressed()
        current_level.draw(screen)
        current_level.update(screen)
        player.draw(screen)
        player.update(key_pressed)
        player.draw_health_bar(screen)
        player.draw_points(screen, points_font)
        player.bullet_group.draw(screen)

        if current_level.boss_defeated == True and isinstance(current_level, Level.Level_1):
            current_level = Level.Level_2(player, IMAGES)
        if current_level.boss_defeated == True and isinstance(current_level, Level.Level_2):

            active_game = False
            current_level = Level.Level_1(player, IMAGES)
            current_level.reset()
        if player.hp <= 0:
            lose.play()
            screen.fill((0, 0, 0))
            current_level.music.stop()

            screen.blit(game_over, game_over_rect)
            pygame.display.flip()
            pygame.time.delay(800)
            active_game = False
            start.set_active(True)
            end.set_active(True)
            current_level = Level.Level_1(player, IMAGES)
            current_level.reset()
            current_level.music.stop()

    else:
        screen.fill((52, 78, 91))
        if start.draw(screen):
            pygame.time.delay(400)
            active_game = True
            start.set_active(False)
            end.set_active(False)
            current_level = Level.Level_1(player, IMAGES)
            current_level.reset()
        if end.draw(screen):
            window_open = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
