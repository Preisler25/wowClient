import pygame
from appConst import game_display


class PressBtn:
    def __init__(self, pos_x, pos_y, wanted_size_x, wanted_size_y, imgUrl):
        self.pos = (pos_x, pos_y)
        self.wanted_size_x = wanted_size_x
        self.wanted_size_y = wanted_size_y
        self.img = pygame.image.load(imgUrl).convert_alpha()
        self.img = pygame.transform.scale(
            self.img, (self.wanted_size_x, self.wanted_size_y))
        self.rect = self.img.get_rect(topleft=self.pos)

    def darw(self):
        game_display.blit(self.img, self.pos)
