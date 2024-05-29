import pygame
from laser import Laser


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player_sprite.png')
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 4
        self.current_direction = "right"
        self.lasers = []
        self.last_shot_time = 0
        self.shot_delay = 1500

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

        self.x = max(0, min(self.x, 1000 - self.image_size[0]))
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def shooting_mech(self):
        laser = Laser(self.x + self.image_size[0] // 2, self.y, (0, 0, 255), "up")
        self.lasers.append(laser)

    def draw_lasers(self, game_screen):
        for laser in self.lasers:
            laser.draw(game_screen)

    def move_lasers(self):
        for laser in self.lasers:
            laser.move()
            if laser.y < 0:
                self.lasers.remove(laser)
