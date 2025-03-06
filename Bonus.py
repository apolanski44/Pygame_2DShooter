import pygame.sprite, os
path2 = os.path.join(os.getcwd(), 'music')

class Bonus(pygame.sprite.Sprite):
    def __init__(self, image, x, y, player):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.player = player
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.used = False
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class hp_potion(Bonus):
    def __init__(self, image, x, y, player):
        super().__init__(image, x, y, player)

    def col_with_player(self):
        if self.rect.colliderect(self.player.collision_rect) and self.used == False:
            potion = pygame.mixer.Sound(os.path.join(path2, 'potion.ogg'))
            potion.play()
            self.kill()
            self.used = True
            self.player.hp += 100
    def update(self):
        self.col_with_player()
class speed_potion(Bonus):
    def __init__(self, image, x, y, player):
        super().__init__(image, x, y, player)

    def col_with_player(self):
        if self.rect.colliderect(self.player.collision_rect) and self.used == False:
            potion = pygame.mixer.Sound(os.path.join(path2, 'potion.ogg'))
            potion.play()
            self.kill()
            self.used = True
            self.player.speed += 1

    def update(self):
        self.col_with_player()

