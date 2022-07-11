# list of all platforms ever
# check all blocks within a 200 x 200 rect for collisions
# toggle all blocks within camera area
# turn off collision for blocks 
import pygame
from src.entities.camera import Camera
from src.entities.platform import Platform

from src.constants import CYAN, YELLOW, MAGENTA, BLUE, RED, GREEN, BLACK

# camera = Camera(0, 0, 1280, 720, screen)


# only platforms within camera view

class PlatformSet:
    def __init__(self):
        self.drawn_platforms = []
        self.working_platforms = []

    def update_platforms(self, camera: Camera, all_platforms):
        for platform in all_platforms:
            if platform not in self.drawn_platforms:
                if pygame.Rect.colliderect(platform.rect, camera.rect):
                    self.drawn_platforms.append(platform)

            if platform in self.drawn_platforms:
                if not pygame.Rect.colliderect(platform.rect, camera.rect):
                    self.drawn_platforms.remove(platform)
