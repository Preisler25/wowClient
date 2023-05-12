import pygame

pygame.init()
font = pygame.font.Font(None, 50)


def debug(text, x=10, y=10):
    debug_surface = pygame.display.get_surface()
    text_surface = font.render(str(text), False, (0, 0, 0))
    debug_rect = text_surface.get_rect(topleft=(x, y))
    pygame.draw.rect(debug_surface, (255, 255, 255), debug_rect)
    debug_surface.blit(text_surface, debug_rect)
