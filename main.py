import pygame
from enemy import Enemy
from player import Player


pygame.init()
game_screen = pygame.display.set_mode((1000, 1000))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 19)
pygame.display.set_caption("Space Wars")
background = pygame.image.load('background.png')
player = Player(450, 900)
enemy = Enemy(450, 0)


run = True
player_shooting = False
game_over = False
win = False


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
            "Press the spacebar to start, and the arrows to move in whatever direction. UP to shoot",
            True,
            (255, 255, 255))
        game_screen.blit(intro_msg, (118, 500))
        pygame.display.update()


def laser_hit(player, enemies):
    global game_over, win
    for laser in player.lasers[:]:
        for enemy in enemies[:]:
            if laser.rect.colliderect(enemy.rect):
                player.lasers.remove(laser)
                enemies.remove(enemy)
                break

    for enemy in enemies:
        for laser in enemy.lasers[:]:
            if laser.rect.colliderect(player.rect):
                game_over = True
                break


intro_screen()

while run:
    game_screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_shooting = not player_shooting

    if not game_over and not win:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.move_direction("right")
        if keys[pygame.K_LEFT]:
            player.move_direction("left")

        if player_shooting:
            player.shooting_mech()

        enemies = [enemy]
        for enemy in enemies[:]:
            enemy.move()
            enemy.shooting_mech()
            enemy.move_lasers()

        player.move_lasers()
        laser_hit(player, enemies)

        player.draw_lasers(game_screen)
        for enemy in enemies[:]:
            enemy.draw_lasers(game_screen)
            game_screen.blit(enemy.image, enemy.rect)

        if len(enemies) == 0:
            win = True

    game_screen.blit(player.image, player.rect)

    if game_over:
        game_over_msg = my_font.render("You lose! Press SPACE to restart or press the RED BUTTON on the top left to quit", True, (255, 0, 0))
        game_screen.blit(game_over_msg, (150, 500))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player = Player(450, 900)
            enemy = Enemy(450, 0)
            player_shooting = False
            game_over = False
            win = False

    if win:
        win_msg = my_font.render("You win! Press SPACE to restart or press the RED BUTTON on the top left to quit", True, (0, 255, 0))
        game_screen.blit(win_msg, (150, 500))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player = Player(450, 900)
            enemy = Enemy(450, 0)
            player_shooting = False
            game_over = False
            win = False

    pygame.display.update()
