# mouse wheel mechanism
# scroll up for state 4 C -> M - > Y -> C
# scroll down for state 5
# C = 0, M = 1, Y = 2

import pygame
from src.gui.load_sprites import toggles, backgrounds

class Toggler:
    def __init__(self):
        self.state = 0
    
    def toggle_clockwise(self):
        if self.state != 2:
            self.state += 1
        else:
            self.state = 0

    def to_blit(self, screen, toggle_pos, bg_pos):
        self.screen = screen
        self.toggle_pos = toggle_pos
        self.bg_pos = bg_pos
        self.screen.blit(backgrounds[self.state], self.bg_pos)
        self.screen.blit(toggles[self.state], self.toggle_pos)

# test blit ---------------------------------------