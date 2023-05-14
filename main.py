import pygame
from debug import debug
from text_to_scr import showText
import random
import time
import math


class PressBtn:
    def __init__(self, pos_x, pos_y, wanted_size_x, wanted_size_y, imgUrl):
        self.pos = (pos_x, pos_y)
        self.wanted_size_x = wanted_size_x
        self.wanted_size_y = wanted_size_y
        self.img = pygame.image.load(imgUrl).convert_alpha()
        self.img = pygame.transform.scale(
            self.img, (self.wanted_size_x, self.wanted_size_y))
        self.rect = self.img.get_rect(topleft=self.pos)

    def darw(self):
        game_display.blit(self.img, self.pos)


class Char:
    def __init__(self, imgUrl):
        self.pos_x = 0
        self.pos_y = 0
        self.img = pygame.image.load(imgUrl).convert_alpha()
        self.rect = self.img.get_rect(topleft=(self.pos_x, self.pos_y))

    def __str__(self):
        return f"pos_x:{self.pos_x}, pos_y:{self.pos_y}"

    def setRandomPos(self, w, h):
        max_width = w-self.img.get_width()
        max_height = h-self.img.get_height()
        self.pos_x = random.randint(0, max_width)
        self.pos_y = random.randint(0, max_height)

    def draw(self):
        game_display.blit(self.img, (self.pos_x, self.pos_y))
        self.rect = self.img.get_rect(topleft=(self.pos_x, self.pos_y))


def dotCh(text, count, dt):
    print(f"con:{count}")
    if count > 0.6:
        count += 1*dt
        text += "."
        count = 0.0
        if text[-4:-1] == "...":
            text = "Press space "
    else:
        count += 1*dt
    return text, count

# ------------------Lobby------------------


def lobby(best_time=100, end_time=100):
    game_exit = False
    pygame.display.set_caption('Lobby')

    # settings some minor variables for the press space text
    counter = 0.0
    press_text = "Press space "

    # settings sin and cos variables
    amplitude = 12
    frequency = 0.2

    # creating settings button
    settings_btn_icon_size = 70
    settings_btn = PressBtn(display_width-settings_btn_icon_size, 0,
                            settings_btn_icon_size, settings_btn_icon_size, "graphics/settings.png")

    # loading background
    bg = pygame.image.load("graphics/menu_bg.jpeg")

    # getting prev time for dt
    prev_time = time.time()

    # display loop
    while not game_exit:

        # getting dt
        dt = time.time() - prev_time
        prev_time = time.time()

        # dot changing for the press space text
        press_text, counter = dotCh(press_text, counter, dt)

        # getting displacement form sin and cos
        displacement_x = amplitude * \
            math.sin(2 * math.pi * frequency * pygame.time.get_ticks() / 300)
        displacement_x = int(displacement_x)

        displacement_y = amplitude * \
            math.cos(2 * math.pi * frequency * pygame.time.get_ticks() / 300)
        displacement_y = int(displacement_y)

        # drawing lobby
        # drawing background
        game_display.blit(bg, (0, 0))
        # Settings button
        settings_btn.darw()
        # Press space text
        showText(press_text, (int(display_width/2-100) + displacement_x),
                 int((display_height/4) + displacement_y), 230)
        # Best time
        showText(f"Best time: {best_time}", int(
            display_width/2-250 + displacement_x), int(display_height/2+50 - displacement_x))
        # Last time
        showText(f"Last time: {end_time}", int(
            display_width/2-200 - displacement_x), int(display_height/2+200 - displacement_y))

        # Event handling
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                game_exit = True
            # keydown
            elif event.type == pygame.KEYDOWN:
                # space
                if event.key == pygame.K_SPACE:
                    # Start games
                    best_time, end_time = gameLoop(best_time)
                    pygame.display.set_caption('Lobby')
            # mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # getting mouse position
                pos = pygame.mouse.get_pos()
                # settings
                if settings_btn.rect.collidepoint(pos):
                    settings_page()
        # Update display
        pygame.display.update()

# ------------------Settings------------------


def settings_page():
    game_exit = False
    pygame.display.set_caption('Settings')

    # loading background
    bg = pygame.image.load("graphics/menu_bg.jpeg")

    # creating back button
    back_icon_size = 50
    back_btn = PressBtn(0, 0, back_icon_size,
                        back_icon_size, "graphics/back.jpg")

    # display loop
    while not game_exit:

        # drawing settings
        # drawing background
        game_display.blit(bg, (0, 0))
        # back button
        back_btn.darw()

        # Event handling
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                game_exit = True
            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # getting mouse position
                pos = pygame.mouse.get_pos()
                # back
                if back_btn.rect.collidepoint(pos):
                    game_exit = True

        pygame.display.update()

# ------------------Game------------------


def gameLoop(best_time):
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
                    print(enemy)
                    # increasing counter
                    counter += 1
            # keydown
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    debug("alma")

        # Update display
        pygame.display.update()

    # getting end time
    endTime = time.time()-start_time
    # testing for new best time
    if endTime < best_time:
        best_time = endTime
    return best_time, endTime


# ------------------Main------------------
 # Initialize Pygame
pygame.init()

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
