import pygame


class Laser:
    def __init__(self, x, y, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.direction = color
        self.image = pygame.Surface((5, 10))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

