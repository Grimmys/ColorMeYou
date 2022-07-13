# blit brightness screen
import pygame
# from src.constants import INCREMENT_OPACITY

from src.entities.entity import Entity

class Brightness(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        self.opacity = 0
        self.color = (0, 0, 0)
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.surface.set_alpha(self.opacity)
    
    def update(self, levels_bar):
        if levels_bar.level == 4:
            self.color = (0, 0, 0)
            self.opacity = 0
        # halfway going down: increase black
        if levels_bar.level < 4:
            self.color = (0, 0, 0)
            # self.opacity += INCREMENT_OPACITY
        # halfway going up: increase white
        if levels_bar.level > 4:
            self.color = (255, 255, 255)
            # self.opacity += INCREMENT_OPACITY

        # self.opacity += INCREMENT_OPACITY

    def draw(self, screen):
        self.surface.fill(self.color)
        self.surface.set_alpha(self.opacity)
        screen.blit(self.surface, (self.rect.x, self.rect.y))

brightness = Brightness(0, 0, 1280, 720)