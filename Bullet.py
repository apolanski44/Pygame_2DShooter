import pygame
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_image, x, y, angle):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10
        self.x_vel = math.cos(self.angle * (2*math.pi/360))* self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_lifetime = 1900
        self.spawn_time = pygame.time.get_ticks()
    def bullet_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill()


    def update(self, *args):
        self.bullet_movement()