import pygame
import math

# settings sin and cos variables
amplitude = 12
frequency = 0.2


def genSin():
    dis_x = amplitude * math.sin(2 * math.pi * frequency *
                                 pygame.time.get_ticks() / 300)
    return int(dis_x)


def genCos():
    dis_y = amplitude * math.cos(2 * math.pi * frequency *
                                 pygame.time.get_ticks() / 300)
    return int(dis_y)
