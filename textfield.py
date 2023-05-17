import pygame
from appConst import screen


class Textfield:
    def __init__(self, x, y, width, height, text, font, color, background_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.color = color
        self.background_color = background_color
        self.rect = pygame.Rect(x, y, width, height)
        self.active = False

    def draw(self):
        pygame.draw.rect(screen.surf, self.background_color, self.rect)
        font = pygame.font.Font(self.font, self.height - 4)
        text = font.render(self.text, True, self.color)
        screen.surf.blit(text, (self.rect.x + 2, self.rect.y + 2))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = (0, 0, 0)
                self.background_color = (255, 255, 255)
            else:
                self.active = False
                self.color = (255, 255, 255)
                self.background_color = (0, 0, 0)
        if event.type == pygame.KEYDOWN:
            print(event.type)
            print(event.key)
            print(event.unicode)
            print(self.active)
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.rect.w = max(100, self.width)
