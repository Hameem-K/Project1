import pygame

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player_sprite.png')
        self.image_size = (50, 50)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        
