import pygame

from src.scenes.scene import Scene

SETTINGS_BACKGROUND = pygame.image.load("assets/images/settings_pop_up.png")


class Settings(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

    def draw(self):
        super().draw()
        self.screen.blit(SETTINGS_BACKGROUND, (0, 0))
