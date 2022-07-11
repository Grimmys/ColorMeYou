# platform class
# drawn with rect
# toggle opacity levels

# one of the following colors:

# cyan
# yellow
# magenta
# blue (cyan + magenta)
# red (magenta + yellow)
# green (cyan + yellow)

import pygame

from src.constants import STRONG_OPACITY, WEAK_OPACITY
from src.entities.entity import Entity


class Platform(Entity):
    def __init__(self, color, x_coord, y_coord, width, height, state: bool):
        super().__init__(x_coord, y_coord, width, height)
        self.color = color
        self.is_active: bool = state
        self.surface = pygame.Surface((self.rect.width, self.rect.height))

    def draw(self, screen):
        self.surface.fill(self.color)
        if not self.is_active:
            self.surface.set_alpha(WEAK_OPACITY)
        else:
            self.surface.set_alpha(STRONG_OPACITY)
        screen.blit(self.surface, (self.rect.x, self.rect.y))
