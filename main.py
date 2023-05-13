import pygame
from debug import debug
import random
import time
import math


def genRandomPos(s_w, s_h):
    p_x = random.randint(0, s_w)
    p_y = random.randint(0, s_h)
    return p_x, p_y


def lobby(best_time=100, end_time=100):
    pygame.display.set_caption('Lobby')
    game_exit = False

    amplitude = 10
    frequency = 0.5

    while not game_exit:
        displacement = amplitude * \
            math.sin(2 * math.pi * frequency * pygame.time.get_ticks() / 1000)
        game_display.fill(black)
        debug("Press space to start", (display_width/2-150) +
              displacement, (display_height/2) + displacement)
        debug(f"Best time: {best_time}",
              display_width/2-150, display_height/2+50)
        debug(f"Last time: {end_time}", display_width/2-150,
              display_height/2+100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    best_time, end_time = gameLoop(best_time)
        pygame.display.update()


def gameLoop(best_time):
    # Load button
    enemy = pygame.image.load(
        'graphics/Player/player_stand.png').convert_alpha()
    w = display_width-enemy.get_width()
    h = display_height-enemy.get_height()

    pygame.display.set_caption('Game')

    pos_x, pos_y = genRandomPos(w, h)
    # Game loop
    game_exit = False
    start_time = time.time()
    counter = 0
    while counter < 10 and not game_exit:

        game_display.fill(black)
        b = game_display.blit(enemy, (pos_x, pos_y))
        # Displaying time and points
        debug(f"Time: {time.time()-start_time}", display_width-170, 10)
        debug(f"Remaining: {10-counter}", display_width/2-75, 10)

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
    endTime = time.time()-start_time
    if endTime < best_time:
        best_time = endTime
    return best_time, endTime


pygame.init()

clock = pygame.time.Clock()

# Display dimensions
display_width = 800
display_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create game display
game_display = pygame.display.set_mode((display_width, display_height))


# Lobby loop
lobby()

# Quit Pygame
pygame.quit()
quit()
