# mouse wheel mechanism
# scroll up for state 4 C -> M - > Y -> C
# scroll down for state 5
# C = 0, M = 1, Y = 2

import pygame
from src.gui.load_sprites import toggles, backgrounds

BG_IMG_POSITION = (-720, -780)
TOGGLER_POSITION = (15, 15)

class Toggler:
    def __init__(self):
        self.state = 0
    
    def toggle_clockwise(self):
        if self.state != 2:
            self.state += 1
        else:
            self.state = 0
    
    def toggle_counterclockwise(self):
        if self.state != 0:
            self.state -= 1
        else:
            self.state = 2    

    def draw(self, screen):
        self.screen = screen
        self.screen.blit(backgrounds[self.state], BG_IMG_POSITION)
        self.screen.blit(toggles[self.state], TOGGLER_POSITION)

# test blit ---------------------------------------