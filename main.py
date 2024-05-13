import pygame
from player import Player

pygame.init()
game_screen = pygame.display.set_mode((736,736))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 12)
pygame.display.set_caption("Space Invaders: Beginner Edition")
background = pygame.image.load('space.png')

player = Player(736, 368)

start = False
end = False
run = True

while run:
    game_screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    if start == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.move_direction("right")
        if keys[pygame.K_a]:
            player.move_direction("left")
