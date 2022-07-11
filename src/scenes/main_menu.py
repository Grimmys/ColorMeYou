# main menu class:
# start button to init new screen
# settings button to init pop-up
# play music

import pygame

from src.gui.button import Button
from src.gui.load_sprites import start_button_img, settings_button_img
from src.scenes.scene import Scene
from src.scenes.settings import Settings
from src.scenes.tutorial import Tutorial

MAIN_MENU_BACKGROUND = pygame.image.load("assets/images/mm.png")


class MainMenu(Scene):
    MUSIC_ALREADY_STARTED = False

    def __init__(self, screen):
        super().__init__(screen)
        self.buttons = [Button(start_button_img, screen, 356, 404, 568, 112, Tutorial),
                        Button(settings_button_img, screen, 356, 528, 568, 112, Settings)]

    def run(self):
        super().run()
        if not MainMenu.MUSIC_ALREADY_STARTED:
            pygame.mixer.music.load("assets/sounds/bg_track.mp3")
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
            MainMenu.MUSIC_ALREADY_STARTED = True

    def draw(self):
        super().draw()
        self.screen.blit(MAIN_MENU_BACKGROUND, (0, 0))
        for button in self.buttons:
            button.detect_hover()

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.next_scene = button.linked_scene(self.screen)
                    if isinstance(self.next_scene, Settings):
                        self.next_scene.scene_bound_to_close_button = MainMenu
                    self.next_scene.run()
                    break
