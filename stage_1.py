#stage 1, or just dummy page to test main menu

import pygame, sys

class Stage:
    def __init__(self, screen):
        self.screen = screen
    
    def run(self):
        print('running instance of stage')
