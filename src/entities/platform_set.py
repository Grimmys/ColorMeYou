# list of all platforms ever
# check all blocks within a 200 x 200 rect for collisions
# toggle all blocks within camera area
# turn off collision for blocks 
import pygame
from src.entities.camera import Camera
from src.entities.platform import Platform

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

# only platforms within camera view

screen_rect = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

class PlatformSet:
    def __init__(self):
        self.drawn_platforms = []
        self.working_platforms = []

    def update_platforms(self, platforms):
        for platform in platforms:
            if platform not in self.drawn_platforms:
                if pygame.Rect.colliderect(platform.rect, screen_rect):
                    self.drawn_platforms.append(platform)

            if platform in self.drawn_platforms:
                if not pygame.Rect.colliderect(platform.rect, screen_rect):
                    self.drawn_platforms.remove(platform)
