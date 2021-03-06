# stage 1

import pygame

from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, SCREEN_WIDTH, \
    SCREEN_HEIGHT, FAILURE_SOUND, SUCCESS_SOUND, DELAY_BEFORE_NEXT_SCENE
from src.entities.camera import Camera
from src.entities.cartridge import Cartridge, Color
from src.entities.cartridge_set import CartridgeSet
from src.entities.paper import Paper
from src.entities.platform_set import PlatformSet
from src.entities.platforms_list import platforms
from src.entities.player import Player
from src.scenes.win_scene import WinScene
from src.gui.load_sprites import lvl_win_1, lvl_win_2
from src.gui.toggler import Toggler
from src.gui.brightness import brightness
# load in three colored backgrounds
# keep track of state stuff
from src.keyboard_setup import RESTART_KEY
from src.scenes.scene import Scene

PLAYER_INITIAL_X_POSITION = platforms[0].rect.width // 2 - PLAYER_WIDTH // 2
PLAYER_INITIAL_Y_POSITION = 300


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.platforms = platforms
        self.player = Player(PLAYER_INITIAL_X_POSITION, PLAYER_INITIAL_Y_POSITION, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.toggler = Toggler()
        self.platform_set = PlatformSet()
        self.cyan_cartridge = Cartridge(Color.CYAN, 2100, -10, 92, 84, True)
        self.magenta_cartridge = Cartridge(Color.MAGENTA, 3750, 590, 92, 84, True)
        self.yellow_cartridge = Cartridge(Color.YELLOW, 5000, -1010, 92, 84, True)
        self.egg_cartridge = Cartridge(Color.EGG, 7300, 600, 96, 95)
        self.all_cartridges = [self.cyan_cartridge, self.magenta_cartridge, self.yellow_cartridge, self.egg_cartridge]
        self.cartridge_set = CartridgeSet(self.all_cartridges)
        self.paper = Paper(7100, 0, 80, 96)
        self.camera = Camera(200, 200, SCREEN_WIDTH - 400, SCREEN_HEIGHT - 200, screen)
        self.moving_entities = []
        for platform in self.platforms:
            self.moving_entities.append(platform)
        for cartridge in self.all_cartridges:
            self.moving_entities.append(cartridge)
        self.moving_entities.append(self.paper)
        self.moving_entities.append(self.player)
        self.timer_until_next_scene = DELAY_BEFORE_NEXT_SCENE
        self.failure_played = False
        self.checkpoint_position = (PLAYER_INITIAL_X_POSITION, PLAYER_INITIAL_Y_POSITION)
        self.current_lvl_win_frame = lvl_win_1
        self.camera.center_camera(self.player, self.moving_entities)

    def update(self):
        super().update()
        self.camera.center_camera(self.player, self.moving_entities)
        # update player
        self.player.update()
        self.player.walk_counter()
        self.player.detect_collision(self.platforms)
        # update platforms
        self.toggler.toggle_platforms(self.platform_set.drawn_platforms)
        self.platform_set.update_platforms(self.platforms)
        # update objectives
        for cartridge in self.all_cartridges:
            if not cartridge.collected:
                if cartridge.detect_collision(self.player) and cartridge.color != Color.EGG:
                    self.checkpoint_position = (cartridge.initial_rect.x, cartridge.initial_rect.y)
        self.paper.stand_counter()
        if self.paper.detect_collision(self.player):
            if self.cartridge_set.check_win():
                SUCCESS_SOUND.play()
                self.paper.collected = True
                self.player.set_inactive()
                self.next_scene = WinScene(self.screen, self.cartridge_set)
            else:
                if not self.failure_played:
                    FAILURE_SOUND.play()
                    self.failure_played = True
        else:
            self.failure_played = False

        self.player.death_event(self.moving_entities)

        if self.player.should_respawn:
            self.restart_level(False, self.checkpoint_position)

        if self.paper.collected and self.timer_until_next_scene == DELAY_BEFORE_NEXT_SCENE // 2:
            self.current_lvl_win_frame = lvl_win_2

    def draw(self):
        super().draw()
        self.toggler.draw_bg(self.screen)
        for platform in self.platform_set.drawn_platforms:
            platform.draw(self.screen)
        for cartridge in self.all_cartridges:
            cartridge.draw(self.screen)
        self.toggler.draw(self.screen)
        if self.paper.collected:
            self.screen.blit(self.current_lvl_win_frame, (self.paper.rect.centerx,
                                                          self.paper.rect.y + self.paper.rect.height - self.current_lvl_win_frame.get_height()))
        else:
            self.paper.draw(self.screen)
            self.player.draw(self.screen)
        brightness.draw(self.screen)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if self.paper.collected:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.player.states[0] = True
            elif event.key == pygame.K_f:
                self.player.states[1] = True
            elif event.key == pygame.K_e:
                self.player.jumping = True
            elif event.key == RESTART_KEY:
                self.restart_level(True)
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

    def restart_level(self, reset_collected_elements: bool,
                      player_reset_position: tuple[int, int] = (PLAYER_INITIAL_X_POSITION, PLAYER_INITIAL_Y_POSITION)):
        self.toggler.reset_state()
        for entity in self.moving_entities:
            entity.reset()
        self.player.spawn(player_reset_position[0], player_reset_position[1])
        if reset_collected_elements:
            for cartridge in self.all_cartridges:
                cartridge.collected = False
            self.paper.collected = False
        self.timer_until_next_scene = DELAY_BEFORE_NEXT_SCENE
        self.camera.center_camera(self.player, self.moving_entities)
