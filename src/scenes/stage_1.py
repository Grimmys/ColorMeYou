# stage 1

import pygame
import sys

from src.entities.player import Player

# load in three colored backgrounds
# keep track of state stuff

yellow_bg = pygame.image.load("assets/images/y_mode_bg.png")
cyan_bg = pygame.image.load("assets/images/c_mode_bg.png")
magenta_bg = pygame.image.load("assets/images/y_mode_bg.png")

# start in bottom left corner of img
bg_img_position = (-720, -780)

player = Player(10, 10, 24, 30)

class Stage:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
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

            player.key_state_listener()
            player.walk_counter()

            self.screen.blit(yellow_bg, bg_img_position)
            player.draw(self.screen)
            
            pygame.display.update()
