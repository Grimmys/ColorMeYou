
# player class
# left and right walk (with decel?)
# jump, with gravity
# collision
# esf controls (for now)

# just return the image that is supposed to be blit and where

import pygame, sys
vec = pygame.math.Vector2

class Player():
    def __init__(self, x, y, x_len, y_len):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(x, y, x_len, y_len)
        # self states listens to keyboard inputs: left, right, up
        self.states = [False, False, False]
        self.face_direction = 1

        self.pos = vec((10, 10))
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)
        self.friction = -0.12

        # blit animation tracker
        self.walk_count = 0
        self.stand_count = 0
    
    # walk_counter

    def key_state_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.states[0] = True
                if event.key == pygame.K_f:
                    self.states[1] = True
                if event.key == pygame.K_e:
                    self.states[2] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.states[0] = False
                if event.key == pygame.K_f:
                    self.states[1] = False
                if event.key == pygame.K_e:
                    self.states[2] = False



    def walk_counter(self):
        # find first item in self.states that is true
        # set idle state
        if self.states == [False, False, False]:
            self.idle == True
        elif True in self.states:
            self.idle == False
            self.face_direction = self.states.index(True)

        if self.idle == False:
            self.walkcount += 1
            self.standcount = 0
        if self.idle == True:
            self.standcount += 1
            self.walkcount = 0
        # number of standing idle frames * 3 frames each 3 * 7 - 1
        if self.standcount > 20:
            self.standcount = 0
        # 3 frames * 4 total - 1
        if self.walkcount > 11:
            self.walkcount = 0



    # determine what img to blit
    def draw(self, screen):
        self.screen = screen



