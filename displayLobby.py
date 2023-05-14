import pygame
import time
from appConst import screen, player
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
    settings_btn = PressBtn(screen.width-settings_btn_icon_size, 0,
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
        screen.drawImg(bg, (0, 0))
        # Settings button
        settings_btn.darw()
        # Press space text
        showText(press_text, int(screen.width/2-100),
                 int(screen.height-100), 230)
        # Best time
        showText(f"Best time: {player.best_time}", int(
            screen.width/2-300 + displacement_x), int(screen.height/2+50 - displacement_x))
        # Last time
        showText(f"Last time: {player.end_time}", int(
            screen.width/2-250 + displacement_y), int(screen.height/2+0 - displacement_y))
        # miss_clicked
        showText(f"Missed_clicks: {player.miss_clicked}", int(
            screen.width/2-50 + displacement_x), int(screen.height/2-100 - displacement_x))
        # played
        showText(f"Games_played: {player.games_played}", int(
            screen.width/2 + displacement_y), int(screen.height/2-150 - displacement_y))

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
