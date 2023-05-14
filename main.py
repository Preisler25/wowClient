import pygame
import time
import math
from debug import debug
from text_to_scr import showText
from appConst import display_width, display_height, game_display
from button import PressBtn
from char import Char
from visuFunc import dotCh
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


main()
