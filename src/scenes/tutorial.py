# tutorial scene
import pygame

from src.scenes.scene import Scene
from src.scenes.stage_1 import Stage

controls_page = pygame.image.load("assets/images/controls_page_esf.png")
mechanics_page = pygame.image.load("assets/images/mechanics_page.png")


class Tutorial(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.click_count = 0
        self.to_blit = controls_page

    def update(self):
        super().update()
        if self.click_count == 2:
            self.next_scene = Stage(self.screen)
            self.next_scene.run()

    def draw(self):
        super().draw()
        self.screen.blit(self.to_blit, (0, 0))

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.to_blit = mechanics_page
            self.click_count += 1
