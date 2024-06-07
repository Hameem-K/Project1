import pygame


class Laser:
    def __init__(self, x, y, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction
        self.image = pygame.Surface((5, 20))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = -5 if self.direction == "up" else 5

    def move(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
