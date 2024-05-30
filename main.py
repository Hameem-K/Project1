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
enemy3 = Enemy(800, 0)

run = True
player_shooting = False


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
            "Press the spacebar to start, A to go left, D to go right (or the respective arrow keys) and UP to shoot",
            True,
            (255, 255, 255))
        game_screen.blit(intro_msg, (45, 0))
        pygame.display.update()


intro_screen()

while run:
    game_screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_shooting = not player_shooting

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_direction("right")
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_direction("left")

    if player_shooting:
        player.shooting_mech()

    enemy.move()
    enemy2.move()
    enemy3.move()

    enemy.shooting_mech()
    enemy2.shooting_mech()
    enemy3.shooting_mech()

    player.move_lasers()
    enemy.move_lasers()
    enemy2.move_lasers()
    enemy3.move_lasers()

    player.draw_lasers(game_screen)
    enemy.draw_lasers(game_screen)
    enemy2.draw_lasers(game_screen)
    enemy3.draw_lasers(game_screen)

    game_screen.blit(player.image, player.rect)
    game_screen.blit(enemy.image, enemy.rect)
    game_screen.blit(enemy2.image, enemy2.rect)
    game_screen.blit(enemy3.image, enemy3.rect)

    pygame.display.update()
