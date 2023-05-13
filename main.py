import pygame
from debug import debug
from text_to_scr import showText
import random
import time
import math


class Char:
    def __init__(self, imgURl):
        self.pos_x = 0
        self.pos_y = 0
        self.img = pygame.image.load(imgURl).convert_alpha()

    def __str__(self):
        return f"pos_x:{self.pos_x}, pos_y:{self.pos_y}"

    def setRandomPos(self, w, h):
        max_width = w-self.img.get_width()
        max_height = h-self.img.get_height()
        self.pos_x = random.randint(0, max_width)
        self.pos_y = random.randint(0, max_height)


def lobby(best_time=100, end_time=100):
    pygame.display.set_caption('Lobby')
    game_exit = False

    amplitude = 12
    frequency = 0.2

    bg = pygame.image.load("graphics/menu_bg.jpeg")

    while not game_exit:

        displacement_x = amplitude * \
            math.sin(2 * math.pi * frequency * pygame.time.get_ticks() / 300)
        displacement_x = int(displacement_x)

        displacement_y = amplitude * \
            math.cos(2 * math.pi * frequency * pygame.time.get_ticks() / 300)
        displacement_y = int(displacement_y)

        game_display.blit(bg, (0, 0))
        start = showText("Press space to start or click on this", (int(display_width/2-250) +
                                                                   displacement_x), int((display_height/4) + displacement_y), 230)
        showText(f"Best time: {best_time}",
                 int(display_width/2-150 + displacement_x), int(display_height/2+50 - displacement_x))
        showText(f"Last time: {end_time}", int(display_width/2-150 - displacement_x),
                 int(display_height/2+200 - displacement_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    best_time, end_time = gameLoop(best_time)
                    pygame.display.set_caption('Lobby')
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start.collidepoint(pos):
                    best_time, end_time = gameLoop(best_time)
                    pygame.display.set_caption('Lobby')
        pygame.display.update()


def gameLoop(best_time):
    # Load enemy
    enemy = Char('graphics/Player/player_stand.png')
    enemy.setRandomPos(display_width, display_height)
    pygame.display.set_caption('Game')

    # Game loop
    game_exit = False
    start_time = time.time()
    counter = 0
    bg = pygame.image.load("graphics/menu_bg.jpeg")
    while counter < 10 and not game_exit:

        game_display.blit(bg, (0, 0))
        b = game_display.blit(enemy.img, (enemy.pos_x, enemy.pos_y))
        showText(f"Time: {time.time()-start_time}", display_width/2-200, 40)
        showText(f"Remaining: {10-counter}", display_width/2-75, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if b.collidepoint(pos):
                    enemy.setRandomPos(display_width, display_height)
                    print(enemy)
                    counter += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    debug("alma")
        pygame.display.update()

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
