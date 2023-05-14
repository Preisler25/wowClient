import pygame
from appConst import game_display
from button import PressBtn

# ------------------Settings------------------


def settings():
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
