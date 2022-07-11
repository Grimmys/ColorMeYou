# mouse wheel mechanism
# scroll up for state 4 C -> M - > Y -> C
# scroll down for state 5
# C = 0, M = 1, Y = 2

import pygame
from src.gui.load_sprites import toggles, backgrounds

from typing import Sequence
from src.entities.platform import Platform

from src.constants import CYAN_MODE, MAGENTA_MODE, YELLOW_MODE

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

    def toggle_platforms(self, platforms: Sequence[Platform]):
        for platform in platforms:
            if self.state == 0:
                if platform.color not in CYAN_MODE:
                    platform.is_active = False
                else:
                    platform.is_active = True
            elif self.state == 1:
                if platform.color not in MAGENTA_MODE:
                    platform.is_active = False
                else:
                    platform.is_active = True
            elif self.state == 2:
                if platform.color not in YELLOW_MODE:
                    platform.is_active = False
                else:
                    platform.is_active = True

    def reset_state(self):
        self.state = 0

    def draw(self, screen):
        screen.blit(backgrounds[self.state], BG_IMG_POSITION)
        screen.blit(toggles[self.state], TOGGLER_POSITION)
