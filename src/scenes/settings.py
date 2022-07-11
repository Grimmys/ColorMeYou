import pygame

from src.gui.button import Button
from src.scenes.scene import Scene

SETTINGS_SCENE_IMAGE = pygame.image.load("assets/images/settings_pop_up.png")
CLOSE_BUTTON_IMAGE = pygame.image.load("assets/images/cross.png")
CLOSE_BUTTON_DISTANCE_TO_BORDER = 20


class Settings(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.position = (self.screen.get_width() // 2 - SETTINGS_SCENE_IMAGE.get_width() // 2,
                         self.screen.get_height() // 2 - SETTINGS_SCENE_IMAGE.get_height() // 2)
        self.close_button = Button(CLOSE_BUTTON_IMAGE, screen,
                                   SETTINGS_SCENE_IMAGE.get_width() - CLOSE_BUTTON_IMAGE.get_width() -
                                   CLOSE_BUTTON_DISTANCE_TO_BORDER + self.position[0],
                                   CLOSE_BUTTON_DISTANCE_TO_BORDER + self.position[1],
                                   CLOSE_BUTTON_IMAGE.get_width(), CLOSE_BUTTON_IMAGE.get_height())
        self.scene_bound_to_close_button = None

    def draw(self):
        super().draw()
        self.screen.blit(SETTINGS_SCENE_IMAGE, self.position)
        self.screen.blit(self.close_button.image, self.close_button.rect)

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.close_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.next_scene = self.scene_bound_to_close_button(self.screen)
                self.next_scene.run()
