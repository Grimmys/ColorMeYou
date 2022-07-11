# cartridge

import pygame
from src.entities.entity import Entity
from src.gui.load_sprites import cartridges
from src.constants import CYAN, MAGENTA, YELLOW, INTERACT_SOUND

# C - 0, M - 1, Y - 2

all_cartridges = []


class Cartridge(Entity):
    def __init__(self, color, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        self.color = color
        self.collected = False
        self.indicator = False
        all_cartridges.append(self)

    def detect_collision(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.collected = True
            INTERACT_SOUND.play()

    def draw(self, screen):
        if not self.collected:
            screen.blit(cartridges[self.color], (self.rect[0], self.rect[1]))
        # draw indicators on screen
        if self.collected:
            if self.color == 0:
                pygame.draw.rect(screen, CYAN, (300, 10, 20, 20))
            if self.color == 1:
                pygame.draw.rect(screen, MAGENTA, (340, 10, 20, 20))
            if self.color == 2:
                pygame.draw.rect(screen, YELLOW, (380, 10, 20, 20))
