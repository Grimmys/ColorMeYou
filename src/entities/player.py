# player class
# left and right walk (with decel?)
# jump, with gravity
# collision
# esf controls (for now)

# just return the image that is supposed to be blit and where
from typing import Sequence

import pygame

from src.constants import FRICTION, ACCELERATION
from src.entities.entity import Entity
from src.entities.platform import Platform
from src.gui.load_sprites import player_right_idle, player_right_walk, player_left_idle, \
    player_left_walk, player_right_jump, player_left_jump

# don't forget character states with interact and death

vec = pygame.math.Vector2


class Player(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        # self states listens to keyboard inputs: left, right, up

        self.states = [False, False, False]
        self.face_direction = 1

        self.velocity = vec(0, 0)
        self.accel = vec(0, 0)

        # blit animation tracker
        self.walk_count = 0
        self.stand_count = 0

        self.idle = False
        self.is_on_ground = False
        self.wall_collide = False

    def spawn(self, x_coord, y_coord):
        self.rect.x = x_coord
        self.rect.y = y_coord

        self.states = [False, False, False]
        self.face_direction = 1

        self.velocity = vec(0, 0)
        self.accel = vec(0, 0)

        self.walk_count = 0
        self.stand_count = 0

        self.idle = False
        self.is_on_ground = False
        self.wall_collide = False

    def detect_collision(self, platforms: Sequence[Platform]):
        self.is_on_ground = False
        self.wall_collide = False
        for platform in platforms:
            if platform.is_active and pygame.Rect.colliderect(self.rect, platform.rect):
                # vertical collision detection
                if self.rect.centery < platform.rect.top:
                    self.rect.y = platform.rect.top - self.rect.height
                    self.velocity.y = 0
                    self.is_on_ground = True
                    return
                # horizontal collision detection
                if self.face_direction == 1:
                    # platform pieces
                    if platform.rect.width > platform.rect.height:
                        if self.rect.centery > platform.rect.left:
                            self.rect.right = platform.rect.left
                            self.velocity.x = 0
                            self.wall_collide = True
                            return
                    # wall pieces
                    elif platform.rect.width < platform.rect.height:
                        if self.rect.right > platform.rect.left:
                            self.rect.right = platform.rect.left
                            self.velocity.x = 0
                            self.wall_collide = True
                            return
                if self.face_direction == 0:
                    if platform.rect.width > platform.rect.height:
                        if self.rect.centery < platform.rect.right:
                            self.rect.left = platform.rect.right
                            self.velocity.x = 0
                            self.wall_collide = True
                            return
                    elif platform.rect.width < platform.rect.height:
                        if self.rect.left < platform.rect.right:
                            self.rect.left = platform.rect.right
                            self.velocity.x = 0
                            self.wall_collide = True
                            return                        

    def update_position(self):
        # reset accel to 0
        self.accel = vec(0, 0.8)
        if not self.wall_collide:
            if self.states[0]:
                self.accel.x = - ACCELERATION
                self.velocity.x -= 1.3
            elif self.states[1]:
                self.accel.x = ACCELERATION
                self.velocity.x += 1.3
        if self.states[2] and self.is_on_ground:
            self.velocity.y = -19
            self.is_on_ground = False
        if not self.states[2] and not self.is_on_ground:
            if self.velocity.y < -5:
                self.velocity.y = -5

        self.accel.x += self.velocity.x * FRICTION
        self.velocity += self.accel
        self.rect.move_ip(self.velocity + 0.5 * self.accel)

    def walk_counter(self):
        # find first item in self.states that is true
        # set idle state
        if self.states == [False, False, False]:
            self.idle = True
        elif True in self.states:
            self.idle = False
            if self.states.index(True) != 2:
                self.face_direction = self.states.index(True)

        if not self.idle:
            self.walk_count += 1
            self.stand_count = 0
        if self.idle:
            self.stand_count += 1
            self.walk_count = 0
        # 7 * 7 - 1
        if self.stand_count > 48:
            self.stand_count = 0
        # 4 * 7 - 1
        if self.walk_count > 27:
            self.walk_count = 0

    # determine what img to blit
    # if not colliding, then falling
    def draw(self, screen):
        if self.idle:
            if self.face_direction == 0:
                screen.blit(player_left_idle[self.stand_count // 7], self.rect)
            elif self.face_direction == 1:
                screen.blit(player_right_idle[self.stand_count // 7], self.rect)
        if not self.idle:
            # if moving left, right, or jumping
            if not self.states[2]:
                if self.face_direction == 0:
                    screen.blit(player_left_walk[self.walk_count // 7], self.rect)
                elif self.face_direction == 1:
                    screen.blit(player_right_walk[self.walk_count // 7], self.rect)
            if self.states[2]:
                if self.face_direction == 0:
                    screen.blit(player_left_jump, self.rect)
                elif self.face_direction == 1:
                    screen.blit(player_right_jump, self.rect)
