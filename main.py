import pygame
import sys
from displayLobby import lobby

# ------------------Main------------------


def main():

    # Initialize Pygame
    pygame.init()

    # Lobby loop
    lobby()

    # Quit Pygame
    pygame.quit()
    quit()
    sys.exit()


main()
