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
    def __init__(self, color, screen, x, y, x_len, y_len, state):
        self.color = color
        self.screen = screen
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, x_len, y_len)
        self.state = state
