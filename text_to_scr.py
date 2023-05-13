import pygame


pygame.init()
font = pygame.font.Font(None, 50)


def showText(text, x=10, y=10, opacity=100, font_color=(0, 0, 0), font_bg_color=None):
    bg_surface = pygame.display.get_surface()
    bg_surface.set_alpha(opacity)
    text_surface = font.render(str(text), False, font_color)
    text_rect = text_surface.get_rect(topleft=(x, y))
    if font_bg_color != None:
        pygame.draw.rect(bg_surface, font_bg_color, text_rect)
    e = bg_surface.blit(text_surface, text_rect)
    return e
