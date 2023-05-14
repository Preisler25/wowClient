import pygame

class Screen:
    def __init__(self, active, width, height):
        self.surf = pygame.display.set_mode((width, height))
        self.active = active
        self.width = width
        self.height = height

    def drawImg(self, img, pos):
        self.surf.blit(img, pos)

    def chScreenView(self):
        if self.active == False:
            self.surf = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.width = pygame.display.Info().current_w
            self.height = pygame.display.Info().current_h
            self.active = True
        else:
            self.width = 800
            self.height = 600
            self.surf = pygame.display.set_mode((self.width, self.height))
            self.active = False