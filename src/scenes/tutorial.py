# tutorial scene
import pygame
import sys

from src.scenes.stage_1 import Stage

controls_page = pygame.image.load("assets/images/controls_page.png")
mechanics_page = pygame.image.load("assets/images/mechanics_page.png")


class Tutorial:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.click_count = 0
        self.to_blit = controls_page
        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.to_blit = mechanics_page
                    self.click_count += 1
                if self.click_count == 2:
                    page_instance = Stage(self.screen)
                    page_instance.run()
                    del page_instance

            self.screen.blit(self.to_blit, (0, 0))

            pygame.display.update()
