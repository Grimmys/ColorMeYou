# stage 1

import pygame

from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, \
    CYAN, YELLOW, MAGENTA, BLUE, RED, GREEN, BLACK
from src.entities.platform import Platform
from src.entities.player import Player

from src.gui.toggler import Toggler

# load in three colored backgrounds
# keep track of state stuff
from src.scenes.scene import Scene
from src.entities.platform import Platform, all_platforms
from src.entities.level_platforms import PlatformSet


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.all_platforms = all_platforms
        self.player = Player(400, 10, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.toggler = Toggler()
        self.platform_set = PlatformSet()

    def update(self):
        super().update()
        self.player.update_position()
        self.player.walk_counter()
        self.player.detect_collision(self.platform_set.working_platforms)
        self.toggler.toggle_platforms(self.platform_set.drawn_platforms)
        self.platform_set.update_platforms()
        print(len(self.all_platforms), len(self.platform_set.working_platforms), \
            len(self.platform_set.drawn_platforms))

    def draw(self):
        super().draw()
        self.toggler.draw(self.screen)
        for platform in self.platform_set.drawn_platforms:
            platform.draw(self.screen)
        self.player.draw(self.screen)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.player.states[0] = True
            if event.key == pygame.K_f:
                self.player.states[1] = True
            if event.key == pygame.K_e:
                self.player.states[2] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.player.states[0] = False
            if event.key == pygame.K_f:
                self.player.states[1] = False
            if event.key == pygame.K_e:
                self.player.states[2] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.toggler.toggle_clockwise()
            if event.button == 5:
                self.toggler.toggle_counterclockwise()
