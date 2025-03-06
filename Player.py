import math
from Bullet import Bullet
import pygame, os
path = os.path.join(os.getcwd(), 'images')
path2 = os.path.join(os.getcwd(), 'music')
class Player(pygame.sprite.Sprite):
    def __init__(self, image, cx, cy, obstacles):
        super().__init__()
        self.base_image = image
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)
        self.shoot_cooldown = 0
        self.points = 0
        self.obstacles = obstacles
        self.hp = 100
        self.speed = 2
        self.max_hp = 100
        self.attack_damage = 25

        self.bullet_group = pygame.sprite.Group()
        self.gun_offset = pygame.math.Vector2(35,0)
        collision_rect_width = 10
        collision_rect_height = 10
        self.collision_rect = pygame.Rect(0, 0, collision_rect_width, collision_rect_height)
        self.mouse_pos = None
        self.x_change_mouse_player = None
        self.y_change_mouse_player = None
        self.angle = None
    def draw_health_bar(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (0, 0, 200, 10))
        pygame.draw.rect(surface, "green", (0, 0, 200 * ratio, 10))
    def draw_points(self, surface, font):
        points = font.render(f'Punkty: {self.points}', True, (255,255,255))
        surface.blit(points, (10, 20))
    def update_collision_rect(self):
        self.collision_rect.center = self.rect.center
    def draw(self, surface):

        surface.blit(self.image, self.rect)
    def shoot(self):
            if self.shoot_cooldown == 0:
                shoot_sound = pygame.mixer.Sound(os.path.join(path2, 'shoot.ogg'))
                shoot_sound.play()
                poss_of_bullet = self.rect.center + self.gun_offset.rotate(self.angle)
                bullet_image = pygame.image.load(os.path.join(path, 'bullet.png')).convert_alpha()
                bullet = Bullet(bullet_image, poss_of_bullet[0], poss_of_bullet[1], self.angle)
                self.bullet_group.add(bullet)
                self.shoot_cooldown = 20

    def player_rotation(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.x_change_mouse_player = self.mouse_pos[0] - self.rect.centerx
        self.y_change_mouse_player = self.mouse_pos[1] - self.rect.centery
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def col_with_obstacles(self):
        for obstacle in self.obstacles:
            if self.collision_rect.colliderect(obstacle):
                return True
        return False

    def update(self, key_pressed):

        old_rect = self.rect.copy()
        self.player_rotation()
        self.get_event(key_pressed)
        self.bullet_group.update()

        if self.col_with_obstacles():
            self.rect = old_rect
        self.update_collision_rect()


        if self.shoot_cooldown > 0:
            self.shoot_cooldown -=1
        if self.rect.bottom > 980:
            self.rect.bottom = 980
        if self.rect.top < 30:
            self.rect.top = 30
        if self.rect.left < 20:
            self.rect.left = 20
        if self.rect.right > 1180:
            self.rect.right = 1180

    def get_event(self, key_pressed):
        mouse_buttons = pygame.mouse.get_pressed()
        old_rect = self.rect.copy()

        if key_pressed[pygame.K_a]:
            self.rect.move_ip(-self.speed, 0)
            self.update_collision_rect()
            if self.col_with_obstacles():
                self.rect = old_rect
                self.update_collision_rect()
        if key_pressed[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
            self.update_collision_rect()
            if self.col_with_obstacles():
                self.rect = old_rect
                self.update_collision_rect()
        if key_pressed[pygame.K_w]:
            self.rect.move_ip(0, -self.speed)
            self.update_collision_rect()
            if self.col_with_obstacles():
                self.rect = old_rect
                self.update_collision_rect()
        if key_pressed[pygame.K_s]:
            self.rect.move_ip(0, self.speed)
            self.update_collision_rect()
            if self.col_with_obstacles():
                self.rect = old_rect
                self.update_collision_rect()

        if mouse_buttons[0]:
            self.shoot()


