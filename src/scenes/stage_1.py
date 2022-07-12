# stage 1

import pygame

from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, MAGENTA, CYAN, BLACK, GREEN, YELLOW, BLUE, SCREEN_WIDTH, \
    SCREEN_HEIGHT, INTERACT_SOUND, DELAY_BEFORE_NEXT_SCENE
from src.entities.camera import Camera
from src.entities.cartridge import Cartridge, Color
from src.entities.cartridge_set import CartridgeSet
from src.entities.paper import Paper
from src.entities.platform import Platform
from src.entities.platform_set import PlatformSet
from src.entities.player import Player
from src.entities.win_scene import WinScene
from src.gui.toggler import Toggler
# load in three colored backgrounds
# keep track of state stuff
from src.keyboard_setup import RESTART_KEY
from src.scenes.scene import Scene

PLAYER_INITIAL_X_POSITION = 100
PLAYER_INITIAL_Y_POSITION = 100


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.platforms = [Platform(BLACK, 0, 540, 1500, 300, True), Platform(CYAN, 400, 440, 200, 40, True),
                          Platform(MAGENTA, 700, 340, 200, 40, False), Platform(YELLOW, 1000, 240, 200, 40, False),
                          Platform(GREEN, 1300, 140, 200, 40, True), Platform(BLUE, 1500, 200, 40, 400, True),
                          Platform(BLACK, 1800, 100, 600, 700, True), Platform(BLUE, 300, 200, 40, 500, True)
                          ]
        self.player = Player(PLAYER_INITIAL_X_POSITION, PLAYER_INITIAL_Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.toggler = Toggler()
        self.platform_set = PlatformSet()
        self.cyan_cartridge = Cartridge(Color.CYAN, 400, 340, 92, 84, True)
        self.magenta_cartridge = Cartridge(Color.MAGENTA, 600, 240, 92, 84, True)
        self.yellow_cartridge = Cartridge(Color.YELLOW, 800, 140, 92, 84, True)
        self.egg_cartridge = Cartridge(Color.EGG, 400, 140, 96, 95)
        self.all_cartridges = [self.cyan_cartridge, self.magenta_cartridge, self.yellow_cartridge, self.egg_cartridge]
        self.cartridge_set = CartridgeSet(self.all_cartridges)
        self.paper = Paper(1100, 100, 80, 96)

        self.camera = Camera(200, 200,  SCREEN_WIDTH - 400, SCREEN_HEIGHT - 200, screen)
        self.moving_entities = []
        for platform in self.platforms:
            self.moving_entities.append(platform)
        for cartridge in self.all_cartridges:
            self.moving_entities.append(cartridge)
        self.moving_entities.append(self.paper)
        self.moving_entities.append(self.player)
        self.timer_until_next_scene = DELAY_BEFORE_NEXT_SCENE

    def update(self):
        super().update()
        # update player
        self.player.update_position()
        self.player.walk_counter()
        self.player.detect_collision(self.platforms)
        # update platforms
        self.toggler.toggle_platforms(self.platform_set.drawn_platforms)
        self.platform_set.update_platforms(self.platforms)
        # update objectives
        for cartridge in self.all_cartridges:
            if not cartridge.collected:
                cartridge.detect_collision(self.player)
        self.paper.stand_counter()
        if self.paper.detect_collision(self.player) and self.cartridge_set.check_win():
            INTERACT_SOUND.play()
            self.paper.collected = True
            self.next_scene = WinScene(self.screen, self.cartridge_set)
        self.camera.box_target_camera(self.player, self.moving_entities)


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
            elif event.key == pygame.K_f:
                self.player.states[1] = True
            elif event.key == pygame.K_e:
                self.player.jumping = True
            elif event.key == RESTART_KEY:
                self.restart_level()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.player.states[0] = False
            elif event.key == pygame.K_f:
                self.player.states[1] = False
            elif event.key == pygame.K_e:
                self.player.jumping = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.toggler.toggle_clockwise()
            elif event.button == 5:
                self.toggler.toggle_counterclockwise()

    def restart_level(self):
        self.player.spawn(PLAYER_INITIAL_X_POSITION, PLAYER_INITIAL_Y_POSITION)
        self.toggler.reset_state()
        self.paper.collected = False
        for cartridge in self.all_cartridges:
            cartridge.collected = False
        self.timer_until_next_scene = DELAY_BEFORE_NEXT_SCENE
