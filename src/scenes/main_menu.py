# main menu class:
# start button to init new screen
# settings button to init pop-up
# play music

import pygame

from src.gui.button import Button
from src.gui.load_sprites import start_button_img, settings_button_img
from src.scenes.scene import Scene
from src.scenes.tutorial import Tutorial

background = pygame.image.load("assets/images/mm.png")


class MainMenu(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.start_button = Button(start_button_img, screen, 356, 404, 568, 112)
        self.settings_button = Button(settings_button_img, screen, 356, 528, 568, 112)

    def run(self):
        super().run()
        pygame.mixer.music.load("assets/sounds/bg_track.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def draw(self):
        super().draw()
        self.screen.blit(background, (0, 0))
        self.start_button.detect_hover()
        self.settings_button.detect_hover()

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_scene = self.start_button.navigate(Tutorial)
