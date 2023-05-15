import pygame
from displayLogin import login

# ------------------Main------------------


def main():

    # Initialize Pygame
    pygame.init()

    # Lobby loop
    login()

    # Quit Pygame
    pygame.quit()
    quit()


main()
