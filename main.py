import pygame
from debug import debug
import random
import time


def genRandomPos(s_w, s_h):
    p_x = random.randint(0, s_w)
    p_y = random.randint(0, s_h)
    return p_x, p_y


def gameLoop():
    pos_x, pos_y = genRandomPos(w, h)
    # Game loop
    game_exit = False
    start_time = time.time()
    counter = 0
    while counter < 10 and not game_exit:

        game_display.fill(black)
        b = game_display.blit(button, (pos_x, pos_y))
        # Displaying time and points
        debug(f"Time: {time.time()-start_time}", display_width-170, 10)
        debug(f"Points: {counter}", display_width/2-75, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if b.collidepoint(pos):
                    pos_x, pos_y = genRandomPos(w, h)
                    counter += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    debug("alma")
        pygame.display.update()

    print("Game over!")


pygame.init()

# Display dimensions
display_width = 800
display_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create game display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')

button = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
w = display_width-button.get_width()
h = display_height-button.get_height()

gameLoop()
gameLoop()

# Quit Pygame
pygame.quit()
quit()
