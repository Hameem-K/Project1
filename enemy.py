import pygame
from laser import Laser


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('enemy_sprite.png')
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 8
        self.direction = "right"
        self.lasers = []
        self.last_shot_time = 0
        self.shot_delay = 250

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

    def shooting_mech(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shot_delay:
            laser = Laser(self.x + self.image_size[0] // 2, self.y + self.image_size[1], (255, 0, 0), "down")
            self.lasers.append(laser)
            self.last_shot_time = current_time

    def draw_lasers(self, game_screen):
        for laser in self.lasers:
            laser.draw(game_screen)

    def move_lasers(self):
        for laser in self.lasers[:]:
            laser.move()
            if laser.y > 1000:
                self.lasers.remove(laser)
