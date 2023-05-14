import pygame
import math
import time
from appConst import game_display, display_width, display_height, best_time, end_time
from button import PressBtn
from text_to_scr import showText
from visuFunc import dotCh
from displaySettings import settings
from displayGame import game
from baseFunc import genSin, genCos


# ------------------Lobby------------------


def lobby():
    game_exit = False
    pygame.display.set_caption('Lobby')

    # settings some minor variables for the press space text
    counter = 0.0
    press_text = "Press space "

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
        displacement_x = genSin()

        displacement_y = genCos()

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
                    game()
                    pygame.display.set_caption('Lobby')
            # mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # getting mouse position
                pos = pygame.mouse.get_pos()
                # settings
                if settings_btn.rect.collidepoint(pos):
                    settings()
        # Update display
        pygame.display.update()
