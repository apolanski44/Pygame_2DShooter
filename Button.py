import pygame


class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.active = True

    def draw(self, surface):
        if self.active:
            surface.blit(self.image, (self.x, self.y))
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                    self.clicked = True
                elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                    self.clicked = False
                    return True
        return False

    def set_active(self, state):
        self.active = state
        self.clicked = False
