# list of all platforms ever
# check all blocks within a 200 x 200 rect for collisions
# toggle all blocks within camera area
# turn off collision for blocks 
import pygame
from src.entities.camera import Camera
from src.entities.platform import Platform, platforms

from src.constants import CYAN, YELLOW, MAGENTA, BLUE, RED, GREEN, BLACK

camera = Camera(0, 0, 720, 1280)

# only platforms within camera view

class PlatformSet:
    def __init__(self):
        self.drawn_platforms = []
        self.working_platforms = []

    def update_platforms(self):
        for platform in platforms:
            if platform not in self.drawn_platforms:
                if pygame.Rect.colliderect(platform.rect, camera.rect):
                    self.drawn_platforms.append(platform)
            if platform not in self.working_platforms:
                if platform.state == True:
                    self.working_platforms.append(platform)
            elif platform in self.drawn_platforms:
                if not pygame.Rect.colliderect(platform.rect, camera.rect):
                    self.drawn_platforms.remove(platform)
            elif platform in self.working_platforms:
                if platform.state == False:
                    self.working_platforms.remove(platform)
        

P1 = Platform(BLACK, 0, 600, 1280, 40, True)
P2 = Platform(CYAN, 100, 500, 200, 40, True)
P3 = Platform(MAGENTA, 200, 400, 200, 40, True)
P4 = Platform(YELLOW, 300, 300, 200, 40, True)
P5 = Platform(RED, 600, 200, 40, 500, True)