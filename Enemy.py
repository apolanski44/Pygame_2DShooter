import pygame, os
path2 = os.path.join(os.getcwd(), 'music')


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, cx, cy, player, obstacles):
        super().__init__()
        self.image = image
        self.obstacles = obstacles
        self.rect = image.get_rect()
        self.rect.center = (cx, cy)
        self.player = player
        self.normal_speed = 2
        self.speed = self.normal_speed
        self.hp = 10
        self.attack_damage = 1
        self.attack_cooldown = 5
        self.attack_cooldown_timer = 0
        self.direction = pygame.math.Vector2()
        self.points_value = 0
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def hunt(self):
        if self.attack_cooldown_timer == 0:
            player_vector = pygame.math.Vector2(self.player.rect.center)
            enemy_vector = pygame.math.Vector2(self.rect.center)
            distance = self.get_distance(player_vector, enemy_vector)
            if distance > 0:
                direction = (player_vector - enemy_vector).normalize()
            else:
                direction = pygame.math.Vector2()
                self.player.hp -= self.attack_damage
                self.attack_cooldown_timer = self.attack_cooldown

            self.rect.center += direction * self.speed
        else:
            self.attack_cooldown_timer -=1
    def col_with_obstacles(self):
        col = False
        for obstacle in self.obstacles:
            if self.rect.colliderect(obstacle):
                self.speed = 1
                col = True
                break
        if col == False:
            self.speed = self.normal_speed


    def update(self, surface):

        self.hunt()
        self.get_dmg()
        self.col_with_obstacles()
    def get_distance(self, vectorP, vectorE):
        return (vectorP - vectorE).magnitude()
    def get_dmg(self):
        death = pygame.mixer.Sound(os.path.join(path2, 'zombie_death.ogg'))
        for bullet in self.player.bullet_group:
            if pygame.sprite.collide_rect(self, bullet):

                self.hp -= self.player.attack_damage
                bullet.kill()
                if self.hp <=0:
                    self.kill()
                    death.play()
                    self.player.points += self.points_value
                    print(self.player.points)
                    break







class Zombie1(Enemy):
    def __init__(self, image, cx, cy, player, obstacles):
        super().__init__(image, cx, cy, player, obstacles)
        self.hp = 50
        self.attack_damage = 10
        self.normal_speed = 3
        self.attack_cooldown = 30
        self.points_value = 15

class Zombie2(Enemy):
    def __init__(self, image, cx, cy, player, obstacles):
        super().__init__(image, cx, cy, player, obstacles)
        self.hp = 150
        self.attack_damage = 25
        self.normal_speed = 1.8
        self.attack_cooldown = 100
        self.points_value = 30

class Headless(Enemy):
    def __init__(self, image, cx, cy, player, obstacles):
        super().__init__(image, cx, cy, player, obstacles)
        self.hp = 75
        self.attack_damage = 20
        self.normal_speed = 2.5
        self.attack_cooldown = 30
        self.points_value = 10

class Boss1(Enemy):
    def __init__(self, image, cx, cy, player, obstacles):
        super().__init__(image, cx, cy, player, obstacles)
        self.hp = 160
        self.attack_damage = 100
        self.max_hp = self.hp
        self.normal_speed = 2
        self.attack_cooldown = 30
        self.points_value = 100

    def draw_health_bar(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (300, 0, 500, 20))
        pygame.draw.rect(surface, "green", (300, 0, 500 * ratio, 20))


class Boss2(Enemy):
    def __init__(self, image, cx, cy, player, obstacles):
        super().__init__(image, cx, cy, player, obstacles)
        self.hp = 500
        self.attack_damage = 100
        self.max_hp = self.hp
        self.normal_speed = 2
        self.attack_cooldown = 30
        self.points_value = 100

    def draw_health_bar(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (300, 0, 500, 20))
        pygame.draw.rect(surface, "green", (300, 0, 500 * ratio, 20))
