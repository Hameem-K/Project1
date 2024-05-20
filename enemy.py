import pygame


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('enemy_sprite.png')
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3.75
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += self.delta
            if self.x + self.image_size[0] >= 1000:
                self.direction = "left"
        elif self.direction == "left":
            self.x -= self.delta
            if self.x <= 0:
                self.direction = "right"
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
