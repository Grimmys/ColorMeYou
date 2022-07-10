# cartridge

import pygame
from src.entities.entity import Entity
from src.gui.load_sprites import cartridges
from src.constants import CYAN, MAGENTA, YELLOW, INTERACT_SOUND
# C - 0, M - 1, Y - 2

cartridge_set = []

class Cartridge(Entity):
    def __init__(self, color, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        self.color = color
        self.state = True
        self.indicator = False
        self.played = False

    def detect_collision(self, player):
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.state = False
            self.indicator = True
            if self.indicator and not self.played:
                INTERACT_SOUND.play()
                self.played = True
    
    def draw(self, screen):
        if self.state:
            screen.blit(cartridges[self.color], (self.rect[0], self.rect[1]))
        if self.indicator:
            if self.color == 0:
                pygame.draw.rect(screen, CYAN, (300, 10, 20, 20))
            if self.color == 1:
                pygame.draw.rect(screen, MAGENTA, (340, 10, 20, 20))
            if self.color == 2:
                pygame.draw.rect(screen, YELLOW, (380, 10, 20, 20))

    

