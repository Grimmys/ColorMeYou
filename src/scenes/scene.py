from typing import Optional

import pygame


class Scene:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.next_scene: Optional[Scene] = None

    def run(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def process_event(self, event: pygame.event.Event):
        pass
