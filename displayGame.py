import pygame
import time
from debug import debug
from text_to_scr import showText
from appConst import display_width, display_height, game_display, player
from char import Char

# ------------------Game------------------


def game():
    game_exit = False
    pygame.display.set_caption('Game')

    # Load enemy
    enemy = Char('graphics/Player/player_stand.png')
    # Setting enemy position randomly but not out of the screen
    enemy.setRandomPos(display_width, display_height)

    # getting start time
    start_time = time.time()

    # setting counter
    counter = 0

    # loading background
    bg = pygame.image.load("graphics/menu_bg.jpeg")

    # Game loop
    while counter < 10 and not game_exit:

        # drawing game
        # drawing background
        game_display.blit(bg, (0, 0))
        # drawing enemy
        enemy.draw()
        print(enemy)
        # drawing time
        showText(f"Time: {time.time()-start_time}", display_width/2-200, 40)
        # drawing counter
        showText(f"Remaining: {10-counter}", display_width/2-75, 10)

        # Event handling
        for event in pygame.event.get():
            # quits
            if event.type == pygame.QUIT:
                game_exit = True
            # mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # getting mouse position
                pos = pygame.mouse.get_pos()
                # if enemy pressed
                if enemy.rect.collidepoint(pos):
                    # setting new enemy position
                    enemy.setRandomPos(display_width, display_height)
                    # increasing counter
                    counter += 1
            # keydown
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    debug("alma")

        # Update display
        pygame.display.update()

    # ending game
    player.end_time = time.time()-start_time
    player.endGame()
