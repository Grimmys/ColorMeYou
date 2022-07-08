# tutorial scene
import pygame

from src.scenes.scene import Scene
from src.scenes.stage_1 import Stage

CONTROLS_PAGE_IMAGE = pygame.image.load("assets/images/controls_page_esf.png")
MECHANICS_PAGE_IMAGE = pygame.image.load("assets/images/mechanics_page.png")


class Tutorial(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.click_count = 0
        self.active_page = CONTROLS_PAGE_IMAGE

    def update(self):
        super().update()
        if self.click_count == 2:
            self.next_scene = Stage(self.screen)
            self.next_scene.run()

    def draw(self):
        super().draw()
        self.screen.blit(self.active_page, (0, 0))

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active_page = MECHANICS_PAGE_IMAGE
            self.click_count += 1
