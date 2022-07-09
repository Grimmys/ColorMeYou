# platform class
# drawn with rect
# toggle opacity levels

# one of the following colors:

# cyan = (1, 176, 239)
# yellow = (255, 247, 1)
# magenta = (237, 0, 140)
# blue (cyan + magenta) = (11, 41, 181)
# red (magenta + yellow) = (169, 0, 46)
# green (cyan + yellow) = (0, 173, 32)

import pygame


class Platform:
    def __init__(self, color, x_coord, y_coord, width, height, state):
        self.color = color
        self.position = (x_coord, y_coord)
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.state = state
