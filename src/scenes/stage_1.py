# stage 1

import pygame

from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, \
    CYAN, YELLOW, MAGENTA, BLUE, RED, GREEN, BLACK
from src.entities.platform import Platform
from src.entities.player import Player
from src.entities.win_scene import WinScene

from src.gui.toggler import Toggler

# load in three colored backgrounds
# keep track of state stuff
from src.scenes.scene import Scene
from src.entities.platform import Platform, all_platforms
from src.entities.platform_set import PlatformSet
from src.entities.cartridge import Cartridge, all_cartridges
from src.entities.cartridge_set import CartridgeSet
from src.entities.paper import Paper


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.all_platforms = all_platforms
        self.player = Player(100, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.toggler = Toggler()
        self.platform_set = PlatformSet()
        self.cyan_cartridge = Cartridge(0, 400, 340, 92, 84)
        self.magenta_cartridge = Cartridge(1, 600, 240, 92, 84)
        self.yellow_cartridge = Cartridge(2, 800, 140, 92, 84)
        self.egg_cartridge = Cartridge(3, 400, 140, 96, 95)
        self.all_cartridges = all_cartridges
        self.cartridge_set = CartridgeSet(self.all_cartridges)
        self.paper = Paper(100, 300, 80, 96, True)

    def update(self):
        super().update()
        # update player
        self.player.update_position()
        self.player.walk_counter()
        self.player.detect_collision(self.platform_set.working_platforms)
        # update platforms
        self.toggler.toggle_platforms(self.platform_set.drawn_platforms)
        self.platform_set.update_platforms()
        # update objectives
        for cartridge in self.all_cartridges:
            cartridge.detect_collision(self.player)
        self.cartridge_set.update_collected()

        # update paper
        self.cartridge_set.check_win()
        self.paper.stand_counter()
        print(self.paper.rect, self.player.rect)

    def draw(self):
        super().draw()
        self.toggler.draw(self.screen)
        for platform in self.platform_set.drawn_platforms:
            platform.draw(self.screen)

        for cartridge in self.all_cartridges:
            cartridge.draw(self.screen)

        self.paper.draw(self.screen)

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
        if self.cartridge_set.no_egg_win:
            self.paper.navigate(self.player, self.screen, WinScene)
        
