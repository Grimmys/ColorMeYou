# papier-san aka. navigator to win screen / next level

import pygame

from src.entities.entity import Entity
from src.gui.load_sprites import paper


class Paper(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        self.collected = False
        self.stand_count = 0

    def stand_counter(self):
        if self.stand_count < 29:
            self.stand_count += 1
        else:
            self.stand_count = 0

    def detect_collision(self, player):
        if not self.collected:
            return pygame.Rect.colliderect(self.rect, player.rect)
        return False

    def draw(self, screen):
        if not self.collected:
            screen.blit(paper[self.stand_count // 10], (self.rect.x, self.rect.y))
