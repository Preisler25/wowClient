import pygame
from debug import debug

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
b = game_display.blit(button,(300,200))

# Game loop
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if b.collidepoint(pos):
                print("Hello")
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
