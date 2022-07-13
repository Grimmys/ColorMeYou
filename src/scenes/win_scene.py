# win scene
import pygame
from src.gui.brightness import brightness

import src.scenes.main_menu as main_menu
from src.scenes.scene import Scene
# import win condition
from src.gui.load_sprites import endscreens


class WinScene(Scene):
    def __init__(self, screen, cartridge_set):
        super().__init__(screen)
        self.cartridge_set = cartridge_set

    def draw(self):
        super().draw()
        # check win condition here
        self.screen.blit(endscreens[0] if not self.cartridge_set.egg_win else endscreens[1], (0, 0))
        brightness.draw(self.screen)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_scene = main_menu.MainMenu(self.screen)
            self.next_scene.run()
