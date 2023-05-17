import pygame
from appConst import screen
from textfield import Textfield

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
    # display loop
    while not game_exit:
        # drawing settings
        # drawing background
        screen.drawImg(bg, (0, 0))
        #drawing inputs
        username_input.draw()
        password_input.draw()

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
                

        pygame.display.update()
