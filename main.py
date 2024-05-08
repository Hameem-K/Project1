import pygame
pygame.init()
game_screen = pygame.display.set_mode((736,736))

background = pygame.image.load('space.png')

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans', 12)
pygame.display.set_caption("Space Invaders: Beginner Edition")

run = True
while run:
    game_screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
