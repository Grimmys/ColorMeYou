# button class
from typing import Type

import pygame

# could probably move this into constants since we will have an interact sound later
from src.scenes.scene import Scene
from src.constants import INTERACT_SOUND


class Button:
    def __init__(self, image, screen, x_coord, y_coord, width, height):
        self.image = image
        self.screen = screen
        self.position = (x_coord, y_coord)
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.played = False

    def detect_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.image, self.position)
            if not self.played:
                INTERACT_SOUND.play()
                self.played = True
        else:
            self.played = False

    # optional, only for start button, put within event loop
    def navigate(self, destination: Type[Scene]):
        self.destination = destination
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            page_instance = self.destination(self.screen)
            page_instance.run()
            return page_instance
        return None
