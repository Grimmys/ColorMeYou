# stage 1

import pygame

from src.entities.player import Player

# load in three colored backgrounds
# keep track of state stuff
from src.scenes.scene import Scene

yellow_bg = pygame.image.load("assets/images/y_mode_bg.png")
cyan_bg = pygame.image.load("assets/images/c_mode_bg.png")
magenta_bg = pygame.image.load("assets/images/y_mode_bg.png")

# start in bottom left corner of img
bg_img_position = (-720, -780)

player = Player(10, 10, 24, 30)


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)

    def update(self):
        super().update()
        print(player.states)
        player.update_position()
        player.walk_counter()

    def draw(self):
        super().draw()
        self.screen.blit(yellow_bg, bg_img_position)
        player.draw(self.screen)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.states[0] = True
                self.face_direction = 0
            if event.key == pygame.K_f:
                player.states[1] = True
                self.face_direction = 1
            if event.key == pygame.K_e:
                player.states[2] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player.states[0] = False
            if event.key == pygame.K_f:
                player.states[1] = False
            if event.key == pygame.K_e:
                player.states[2] = False
