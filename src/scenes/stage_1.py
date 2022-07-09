# stage 1

import pygame

from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, CYAN
from src.entities.platform import Platform
from src.entities.player import Player

from src.gui.toggler import Toggler

# load in three colored backgrounds
# keep track of state stuff
from src.scenes.scene import Scene

yellow_bg = pygame.image.load("assets/images/y_mode_bg.png")
cyan_bg = pygame.image.load("assets/images/c_mode_bg.png")
magenta_bg = pygame.image.load("assets/images/y_mode_bg.png")

# start in bottom left corner of img


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.platforms = [Platform(CYAN, 0, 500, 1000, 40, True)]
        self.player = Player(10, 10, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.toggler = Toggler()

    def update(self):
        super().update()
        print(self.player.states, self.player.rect)
        self.player.update_position()
        self.player.walk_counter()
        self.player.detect_collision(self.platforms)

    def draw(self):
        super().draw()
        self.toggler.draw(self.screen)
        for platform in self.platforms:
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
