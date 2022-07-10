# list of all platforms ever
# check all blocks within a 200 x 200 rect for collisions
# toggle all blocks within camera area
# turn off collision for blocks 
import pygame
from src.entities.camera import Camera
from src.entities.platform import Platform, all_platforms

from src.constants import CYAN, YELLOW, MAGENTA, BLUE, RED, GREEN, BLACK

camera = Camera(0, 0, 1280, 720)

# only platforms within camera view

class PlatformSet:
    def __init__(self):
        self.drawn_platforms = []
        self.working_platforms = []

    def update_platforms(self):
        for platform in all_platforms:
            if platform not in self.drawn_platforms:
                if pygame.Rect.colliderect(platform.rect, camera.rect):
                    self.drawn_platforms.append(platform)

            if platform not in self.working_platforms:
                if platform.state == True:
                    self.working_platforms.append(platform)

            if platform in self.drawn_platforms:
                if not pygame.Rect.colliderect(platform.rect, camera.rect):
                    self.drawn_platforms.remove(platform)

            if platform in self.working_platforms:
                if platform.state == False:
                    self.working_platforms.remove(platform)
        

P1 = Platform(BLACK, 0, 540, 300, 300, True)
# P2 = Platform(CYAN, 400, 440, 200, 40, True)
P3 = Platform(MAGENTA, 700, 340, 200, 40, False)
P4 = Platform(YELLOW, 1000, 240, 200, 40, False)
P5 = Platform(GREEN, 1300, 140, 200, 40, True)
P6 = Platform(BLUE, 1500, 200, 40, 400, True)
P7 = Platform(BLACK, 1800, 100, 600, 700, True)

test_plat = Platform(BLUE, 300, 200, 40, 500, True)