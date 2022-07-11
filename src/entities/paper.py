# papier-san aka. navigator to win screen / next level

from typing import Type

import pygame

from src.entities.entity import Entity
from src.scenes.scene import Scene
from src.gui.load_sprites import paper, lvl_win

class Paper(Entity):
    def __init__(self, x_coord, y_coord, width, height, state):
        super().__init__(x_coord, y_coord, width, height)
        self.state = state
        self.stand_count = 0

    def stand_counter(self):
        if self.stand_count < 29:
            self.stand_count += 1
        else:
            self.stand_count = 0

    def navigate(self, player, screen, destination: Type[Scene]):
        
        self.destination = destination
        self.screen = screen
        
        if pygame.Rect.colliderect(self.rect, player.rect):
            self.state = False
            screen.blit(lvl_win[0], (self.rect.x, self.rect.y))
            screen.blit(lvl_win[1], (self.rect.x, self.rect.y))
            page_instance = self.destination(self.screen)
            page_instance.run()
            return page_instance
        return None


    def draw(self, screen):
        if self.state == True:
            screen.blit(paper[self.stand_count // 10], (self.rect.x, self.rect.y))
