import pygame
from pygame import Vector2
import sys
from debug import debug
from con import connect

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("WOW 2.0")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

bg_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("Hello World!", False, (255, 255, 255))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_position = Vector2(100, 260)

prev_time = pygame.time.get_ticks()

while True:
    connect()
    current_time = pygame.time.get_ticks()
    dt = current_time - prev_time
    prev_time = current_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    snail_position.x += 200 * dt / 1000

    screen.blit(bg_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (100, 100))
    screen.blit(snail_surface, round(snail_position))

    pygame.display.update()
    clock.tick(600)
