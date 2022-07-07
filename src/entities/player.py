# player class
# left and right walk (with decel?)
# jump, with gravity
# collision
# esf controls (for now)

# just return the image that is supposed to be blit and where

import pygame

vec = pygame.math.Vector2


class Player:
    def __init__(self, x_coord, y_coord, width, y_len):
        self.x = int(x_coord)
        self.y = int(y_coord)
        self.rect = pygame.Rect(x_coord, y_coord, width, y_len)
        # self states listens to keyboard inputs: left, right, up
        self.states = [False, False, False]
        self.face_direction = 1

        self.position = vec((10, 10))
        self.velocity = vec(0, 0)
        self.accel = vec(0, 0)
        self.ACCELERATION = 0.5
        self.FRICTION = -0.12

        # blit animation tracker
        self.walk_count = 0
        self.stand_count = 0

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

    def move(self):
        # reset accel to 0
        self.accel = vec(0, 0)
        if self.states[0]:
            self.accel.x = -self.ACCELERATION
        if self.states[1]:
            self.accel.x = self.ACCELERATION

        self.accel.x += self.velocity.x * self.FRICTION
        self.velocity += self.accel
        self.position += self.velocity + 0.5 * self.accel

    def walk_counter(self):
        # find first item in self.states that is true
        # set idle state
        if self.states == [False, False, False]:
            self.idle = True
        elif True in self.states:
            self.idle = False
            self.face_direction = self.states.index(True)

        if not self.idle:
            self.walk_count += 1
            self.stand_count = 0
        if self.idle:
            self.stand_count += 1
            self.walk_count = 0
        # number of standing idle frames * 3 frames each 3 * 7 - 1
        if self.stand_count > 20:
            self.stand_count = 0
        # 3 frames * 4 total - 1
        if self.walk_count > 11:
            self.walk_count = 0

    # determine what img to blit
    def draw(self, screen):
        self.screen = screen
