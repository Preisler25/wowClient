import pygame
from debug import debug
import random

def genRandomPos(s_w, s_h):
    p_x = random.randint(0, s_w)
    p_y = random.randint(0, s_h)
    return p_x, p_y

pygame.init()

# Display dimensions
display_width = 800
display_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create game display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')

button = pygame.image.load('graphics\Player\player_stand.png').convert_alpha()
w = display_width-button.get_width()
h = display_height-button.get_height()
pos_x, pos_y = genRandomPos(w, h)

# Game loop
game_exit = False

while not game_exit:
    game_display.fill(black)
    b = game_display.blit(button,(pos_x ,pos_y))
    debug(f"{pos_x} {pos_y}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if b.collidepoint(pos):
                pos_x, pos_y = genRandomPos(w, h)
                print("hello")
                debug(f"{pos_x}, {pos_y}")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                debug("alma")
            elif event.key == pygame.K_DOWN:
                debug("körte")
            elif event.key == pygame.K_LEFT:
                debug("alma")
            elif event.key == pygame.K_RIGHT:
                debug("alma")
            
    # Draw game objects
    # ...

    # Update display
    pygame.display.update()


# Quit Pygame
pygame.quit()
quit()
