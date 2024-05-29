import pygame
from player import Player
from enemy import Enemy
from laser import Laser

pygame.init()
game_screen = pygame.display.set_mode((1000, 1000))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 19)
pygame.display.set_caption("Space Wars")
background = pygame.image.load('background.png')
player = Player(450, 900)
enemy = Enemy(500, 0)
enemy2 = Enemy(200, 0)

run = True


def intro_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        game_screen.blit(background, (0, 0))
        intro_msg = my_font.render(
            "Press the spacebar to start, A to go left, D to go right (or use the arrow keys) and up arrow key to shoot",
            True,
            (255, 255, 255))
        game_screen.blit(intro_msg, (35, 0))
        pygame.display.update()


intro_screen()

while run:
    game_screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_direction("right")
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_direction("left")

    enemy.move()
    enemy2.move()

    game_screen.blit(player.image, player.rect)
    game_screen.blit(enemy.image, enemy.rect)
    game_screen.blit(enemy2.image, enemy2.rect)

    pygame.display.update()
