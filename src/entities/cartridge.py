# cartridge
from enum import Enum

import pygame

from src.constants import CYAN, MAGENTA, YELLOW, INTERACT_SOUND
from src.entities.entity import Entity
from src.gui.load_sprites import cartridges


class Color(Enum):
    CYAN = 0
    MAGENTA = 1
    YELLOW = 2
    EGG = 3


class Cartridge(Entity):
    def __init__(self, color: Color, x_coord, y_coord, width, height, is_required=False):
        super().__init__(x_coord, y_coord, width, height)
        self.color = color
        self.collected = False
        self.is_required = is_required

    def detect_collision(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.collected = True
            INTERACT_SOUND.play()
            return True
        return False

    def draw(self, screen):
        if not self.collected:
            screen.blit(cartridges[self.color.value], (self.rect[0], self.rect[1]))
        # draw indicators on screen
        if self.collected:
            if self.color == Color.CYAN:
                pygame.draw.rect(screen, CYAN, (300, 10, 20, 20))
            if self.color == Color.MAGENTA:
                pygame.draw.rect(screen, MAGENTA, (340, 10, 20, 20))
            if self.color == Color.YELLOW:
                pygame.draw.rect(screen, YELLOW, (380, 10, 20, 20))
