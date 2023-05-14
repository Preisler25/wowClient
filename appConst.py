import pygame
from player import Player

# Display dimensions
display_width = 800
display_height = 600

player = Player("username", "password", "email", 100, 100, 0, 0)

# Create game display
game_display = pygame.display.set_mode((display_width, display_height))
