import pygame
from appConst import screen
from button import PressBtn

# ------------------Settings------------------


def settings():
    game_exit = False
    pygame.display.set_caption('Settings')

    # loading background
    bg = pygame.image.load("graphics/menu_bg.jpeg")

    # creating fullscr button
    full_scr_btn_icon_size_x = 70
    full_scr_btn_icon_size_y = 50
    full_scr_btn = PressBtn(screen.width-full_scr_btn_icon_size_x, 0, full_scr_btn_icon_size_x, full_scr_btn_icon_size_y, "graphics/full_scr.png")

    # creating back button
    back_icon_size = 50
    back_btn = PressBtn(0, 0, back_icon_size,
                        back_icon_size, "graphics/back.jpg")

    # display loop
    while not game_exit:
        # drawing settings
        # drawing background
        screen.drawImg(bg, (0, 0))
        # back button
        back_btn.darw()
        # full screen btn
        full_scr_btn.setRight()
        full_scr_btn.darw()

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
                if full_scr_btn.rect.collidepoint(pos):
                    screen.chScreenView()

        pygame.display.update()
