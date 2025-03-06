import pygame
import random
import Enemy
import Bonus
import os
path2 = os.path.join(os.getcwd(), 'music')
class Level:
    def __init__(self, player, images):
        self.player = player
        self.images = images
        self.boss_spawned = False
        self.boss = None
        self.boss_defeated = None
        self.enemy_group = pygame.sprite.Group()
        self.bonus_group = pygame.sprite.Group()
        self.text = self.images['WAVECLEARED']
        self.text_rect = self.text.get_rect(center=(1200 // 2, 1000 // 2))
        self.is_played = False
        self.obstacles = [
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

    def draw(self, surface):
        self.enemy_group.draw(surface)
        self.bonus_group.draw(surface)
    def reset(self):
        self.player.hp = 100
        self.player.speed = 2
        self.player.rect.center = (400, 400)
        self.player.points = 0
        self.player.bullet_group.empty()
        self.bonus_group.empty()
        self.boss_spawned = False
        self.boss = None
        self.boss_defeated = None
        self.is_played = False




class Level_1(Level):
    def __init__(self, player, images):
        super().__init__(player, images)
        self.speed_potion_used = False
        self.hp_potion_used = False
        self.boss_spawned = False
        self.boss = None
        self.boss_defeated = False
        self.is_played = False
        self.music = pygame.mixer.Sound(os.path.join(path2, 'music.ogg'))

    def update(self, surface):
        self.bonus_group.update()
        self.enemy_group.update(surface)

        for enemy in self.enemy_group:
            if enemy.hp <= 0:
                self.enemy_group.remove(enemy)

        while len(self.enemy_group) < 4:
            cx = random.randint(300,900)
            cy = random.randint(300, 900)
            enemy_type = random.choice([
                Enemy.Zombie1(self.images['ZOMBIE1'], cx, cy, self.player, self.obstacles),
                Enemy.Zombie2(self.images['ZOMBIE2'], cx, cy, self.player, self.obstacles),
                Enemy.Headless(self.images['HEADLESS'], cx, cy, self.player, self.obstacles)
            ])
            self.enemy_group.add(enemy_type)

        if self.player.points >= 20 and self.speed_potion_used == False:
            self.bonus_group.add((Bonus.speed_potion(self.images['SPEED'],300, 300, self.player)))
            self.speed_potion_used = True
        if self.player.points >= 30 and self.hp_potion_used == False:
            self.bonus_group.add((Bonus.hp_potion(self.images['SERCE'],600, 600, self.player)))
            self.hp_potion_used = True

        if self.player.points >=10 and self.boss_spawned == False:
            self.boss = Enemy.Boss1(self.images['BOSS2'], 1000, 500, self.player, self.obstacles)
            self.enemy_group.add(self.boss)
            self.boss_spawned = True
        if self.boss_spawned == True:
            self.boss.draw_health_bar(surface)



        if self.boss_spawned == True and self.is_played == False:
            self.music.play()
            self.is_played = True



        if self.boss and self.boss.hp <=0:
            surface.fill((52, 78, 91))
            surface.blit(self.text, self.text_rect)
            pygame.display.flip()
            pygame.time.delay(4000)
            self.enemy_group.remove(self.boss)
            self.boss = None
            self.player.points = 0
            self.player.bullet_group.empty()
            self.enemy_group.empty()
            self.bonus_group.empty()
            self.boss_defeated = True
            self.boss_spawned = False
            self.music.stop()

class Level_2(Level):
    def __init__(self, player, images):
        super().__init__(player, images)
        self.speed_potion_used = False
        self.hp_potion_used = False
        self.boss_spawned = False
        self.boss = None
        self.boss_defeated = False
        self.is_played = False
        self.music = pygame.mixer.Sound(os.path.join(path2, 'music.ogg'))

    def update(self, surface):
        self.bonus_group.update()
        self.enemy_group.update(surface)

        for enemy in self.enemy_group:
            if enemy.hp <= 0:
                self.enemy_group.remove(enemy)

        while len(self.enemy_group) <= 4:
            cx = random.randint(300, 900)
            cy = random.randint(300, 900)
            enemy_type = random.choice([
                Enemy.Zombie1(self.images['ZOMBIE1'], cx, cy, self.player, self.obstacles),
                Enemy.Zombie2(self.images['ZOMBIE2'], cx, cy, self.player, self.obstacles),
                Enemy.Headless(self.images['HEADLESS'], cx, cy, self.player, self.obstacles)
            ])
            self.enemy_group.add(enemy_type)

        if self.player.points >= 20 and self.speed_potion_used == False:
            self.bonus_group.add((Bonus.speed_potion(self.images['SPEED'], 300, 300, self.player)))
            self.speed_potion_used = True
        if self.player.points >= 30 and self.hp_potion_used == False:
            self.bonus_group.add((Bonus.hp_potion(self.images['SERCE'], 600, 600, self.player)))
            self.hp_potion_used = True

        if self.player.points >= 10 and self.boss_spawned == False:
            self.boss = Enemy.Boss2(self.images['BOSS1'], 1000, 500, self.player, self.obstacles)
            self.enemy_group.add(self.boss)
            self.boss_spawned = True
        if self.boss_spawned == True:
            self.boss.draw_health_bar(surface)
        if self.boss_spawned == True and self.is_played == False:
            self.music.play()
            self.is_played = True

        if self.boss and self.boss.hp <=0:
            self.music.stop()
            surface.fill((52, 78, 91))
            self.enemy_group.remove(self.boss)
            self.boss = None
            self.player.points = 0
            self.player.bullet_group.empty()
            self.enemy_group.empty()
            self.bonus_group.empty()
            self.boss_defeated = True
            self.boss_spawned = False


