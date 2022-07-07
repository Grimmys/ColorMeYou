# main menu class:
# start button to init new screen
# settings button to init pop-up
# play music

import pygame, sys
from stage_1 import Stage
from button import Button
from load_sprites import start_button_img, settings_button_img

background = pygame.image.load('assets\images\mm.png')

class MainMenu():
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.start_button = Button(start_button_img, screen, 356, 404, 568, 112)
        self.settings_button = Button(settings_button_img, screen, 356, 528, 568, 112)

    def run(self):
        pygame.mixer.music.load('assets\sounds\\bg_track.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        self.run = True
        while self.run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_button.navigate(Stage)

            self.screen.blit(background, (0, 0))
            self.start_button.detect_hover()
            self.settings_button.detect_hover()

            pygame.display.update()
