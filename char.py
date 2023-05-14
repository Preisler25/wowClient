import pygame
import random
from appConst import game_display


class Char:
    def __init__(self, imgUrl):
        self.pos_x = 0
        self.pos_y = 0
        self.img = pygame.image.load(imgUrl).convert_alpha()
        self.rect = self.img.get_rect(topleft=(self.pos_x, self.pos_y))

    def __str__(self):
        return f"pos_x:{self.pos_x}, pos_y:{self.pos_y}, rect:{self.rect}"

    def setRandomPos(self, w, h):
        max_width = w-self.img.get_width()
        max_height = h-self.img.get_height()
        self.pos_x = random.randint(0, max_width)
        self.pos_y = random.randint(0, max_height)

    def draw(self):
        game_display.blit(self.img, (self.pos_x, self.pos_y))
        self.rect = self.img.get_rect(topleft=(self.pos_x, self.pos_y))
