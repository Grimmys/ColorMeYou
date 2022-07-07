#stage 1, or just dummy page to test main menu

import pygame, sys

# load in three colored backgrounds
# keep track of state stuff

yellow_bg = pygame.image.load('assets\images\y_mode_bg.png')
cyan_bg = pygame.image.load('assets\images\c_mode_bg.png')
magenta_bg = pygame.image.load('assets\images\y_mode_bg.png')

# start in bottom left corner of img
bg_img_position = (-720, -780)

class Stage:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
    
    def run(self):
        self.run = True
        while self.run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.screen.blit(yellow_bg, bg_img_position)
            pygame.display.update()

