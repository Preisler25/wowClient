import pygame
from appConst import screen
from textfield import Textfield
from button import PressBtn
from displayLobby import lobby
from servFunc import sendLogin
# ------------------Settings------------------


def login():
    game_exit = False
    pygame.display.set_caption('Login')

    # loading background
    bg = pygame.image.load("graphics/menu_bg.jpeg")

    # creating  username input
    username_input = Textfield(
        screen.width/2-100, 100, 200, 50, "Username", None)

    # creating password input
    password_input = Textfield(
        screen.width/2-100, 200, 200, 50, "Password", None)
    
    # creating login button
    login_btn = PressBtn(screen.width/2-100, 300, 200, 50, "graphics/login.png")
    # display loop
    while not game_exit:
        # drawing settings
        # drawing background
        screen.drawImg(bg, (0, 0))
        #drawing inputs
        username_input.draw()
        password_input.draw()
        #drawing login button
        login_btn.darw()
        # Event handling
        for event in pygame.event.get():
            #testing inputs
            username_input.update(event)
            password_input.update(event)

            # quit
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit = True
            # mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # getting mouse position
                pos = pygame.mouse.get_pos()
                # back
                if login_btn.rect.collidepoint(pos):
                    if sendLogin(username_input.text, password_input.text):
                        lobby()
                        game_exit = True
                    
                

        pygame.display.update()
