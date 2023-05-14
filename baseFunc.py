import pygame
import math

# settings sin and cos variables
amplitude = 7
frequency = 0.1


def genSin():
    dis_x = amplitude * math.sin(2 * math.pi * frequency *
                                 pygame.time.get_ticks() / 100)
    return int(dis_x)


def genCos():
    dis_y = amplitude * math.cos(2 * math.pi * frequency *
                                 pygame.time.get_ticks() / 100)
    return int(dis_y)
