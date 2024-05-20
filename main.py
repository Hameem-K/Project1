import pygame
from player import Player
from enemy import Enemy

pygame.init()
game_screen = pygame.display.set_mode((1000, 1000))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 12)
pygame.display.set_caption("Space Wars")
background = pygame.image.load('background.png')
player = Player(450, 900)
enemy = Enemy(450, 0)

run = True

while run:
    game_screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.move_direction("right")
    if keys[pygame.K_a]:
        player.move_direction("left")

    enemy.move()

    game_screen.blit(player.image, player.rect)
    game_screen.blit(enemy.image, enemy.rect)

    pygame.display.update()
