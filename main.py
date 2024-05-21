import pygame
from player import Player
from enemy import Enemy

pygame.init()
game_screen = pygame.display.set_mode((1000, 1000))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)
pygame.display.set_caption("Space Wars")
background = pygame.image.load('background.png')
player = Player(450, 900)
enemy = Enemy(500, 0)
enemy2 = Enemy(200, 0)
enemy3 = Enemy(350, 0)
enemy4 = Enemy(650, 0)
run = True


def intro_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        game_screen.blit(background, (0, 0))
        intro_msg = my_font.render("Press the spacebar to start, A to go left, and D to go right", True,
                                   (255, 255, 255))
        game_screen.blit(intro_msg, (235, 500))
        pygame.display.update()


intro_screen()

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
    enemy2.move()
    enemy3.move()
    enemy4.move()

    game_screen.blit(player.image, player.rect)
    game_screen.blit(enemy.image, enemy.rect)
    game_screen.blit(enemy2.image, enemy2.rect)
    game_screen.blit(enemy3.image, enemy3.rect)
    game_screen.blit(enemy4.image, enemy4.rect)

    pygame.display.update()
