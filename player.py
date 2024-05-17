import pygame

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player_sprite.png')
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1
        self.current_direction = "right"

    def move_direction(self, direction):
        if direction == "right" and self.current_direction != "right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = "right"
        elif direction == "left" and self.current_direction != "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = "left"
        if self.current_direction == "right":
            self.x += self.delta
        elif self.current_direction == "left":
            self.x -= self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])



