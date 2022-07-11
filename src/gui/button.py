# button class
from typing import Type

import pygame

from src.scenes.scene import Scene
from src.constants import INTERACT_SOUND


class Button:
    def __init__(self, image, screen, x_coord, y_coord, width, height, linked_scene = None):
        self.image = image
        self.screen = screen
        self.position = (x_coord, y_coord)
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.linked_scene = linked_scene
        self.played = False

    def detect_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.image, self.position)
            if not self.played:
                INTERACT_SOUND.play()
                self.played = True
        else:
            self.played = False
