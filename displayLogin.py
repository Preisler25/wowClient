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
        100, 100, 200, 50, "Username", None, (0, 0, 0), (255, 255, 255))

    # display loop
    while not game_exit:
        # drawing settings
        # drawing background
        screen.drawImg(bg, (0, 0))
        # username input
        username_input.draw()

        # Event handling
        for event in pygame.event.get():
            #testing input
            username_input.update(event)

            # quit
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit = True
                

        pygame.display.update()
