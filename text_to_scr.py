import pygame


pygame.init()
font = pygame.font.Font(None, 50)


def showText(text, x=10, y=10, font_color=(0, 0, 0), font_bg_color=(255, 255, 255)):
    bg_surface = pygame.display.get_surface()
    text_surface = font.render(str(text), False, font_color)
    text_rect = text_surface.get_rect(topleft=(x, y))
    pygame.draw.rect(bg_surface, font_bg_color, text_rect)
    e = bg_surface.blit(text_surface, text_rect)
    return e
