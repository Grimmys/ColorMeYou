# player class
# left and right walk (with decel?)
# jump, with gravity
# collision
# esf controls (for now)

# just return the image that is supposed to be blit and where
from typing import Sequence

import pygame

from src.constants import DEATH_SOUND, FRICTION, ACCELERATION, GRAVITY_VEC, DELAY_BEFORE_RESPAWN
from src.entities.entity import Entity
from src.entities.platform import Platform
from src.gui.load_sprites import player_right_idle, player_right_walk, player_left_idle, \
    player_left_walk, player_right_jump, player_left_jump, player_death

# don't forget character states with interact and death

vec = pygame.math.Vector2

LEFT = 0
RIGHT = 1


class Player(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        # self states listens to keyboard inputs: left, right, up

        self.spawn()

    def spawn(self, x_coord=None, y_coord=None):
        if x_coord is not None:
            self.rect.x = x_coord
        if y_coord is not None:
            self.rect.y = y_coord

        self.states = [False, False]
        self.jumping = False
        self.face_direction = RIGHT

        self.velocity = vec(0, 0)
        self.accel = vec(0, 0)

        self.walk_count = 0
        self.stand_count = 0

        self.idle = False
        self.is_on_ground = False
        self.wall_collide = False

        self.death = False
        self.should_respawn = False
        self._timer_until_respawn = DELAY_BEFORE_RESPAWN
        self.freefall_count = 0

        self.death_played = False

    def detect_collision(self, platforms: Sequence[Platform]):
        self.is_on_ground = False
        self.wall_collide = False
        for platform in platforms:
            if platform.is_active and pygame.Rect.colliderect(self.rect, platform.rect):
                self.handle_collision(platform)

    def handle_collision(self, platform):
        # vertical collision detection
        if self.rect.centery < platform.rect.top and platform.rect.x <= self.rect.centerx <= platform.rect.x + platform.rect.width:
            self.rect.y = platform.rect.top - self.rect.height
            self.velocity.y = 0
            self.is_on_ground = True
            return
        # horizontal collision detection
        if platform.rect.y <= self.rect.centery <= platform.rect.y + platform.rect.height:
            if self.rect.centerx < platform.rect.left:
                self.rect.right = platform.rect.left
                self.velocity.x = 0
                self.wall_collide = True
                return
            if self.rect.centerx > platform.rect.right:
                self.rect.left = platform.rect.right
                self.velocity.x = 0
                self.wall_collide = True
                return

    def death_event(self, moving_entities):
        # if pygame.Rect.colliderect(self.rect, death_line.rect):
        #     self.death = True
        # else:
        #     self.death = False
        if not self.death:
            if not self.is_on_ground and not self.wall_collide:
                self.freefall_count += 1
            else:
                self.freefall_count = 0

            if self.freefall_count == 120:
                self.death = True
                self.accel = GRAVITY_VEC.copy()
                DEATH_SOUND.play()

    def update(self):
        if not self.death:
            self.update_position()
        else:
            self._timer_until_respawn -= 1
            if self._timer_until_respawn <= 0:
                self.should_respawn = True

    def update_position(self):
        # reset accel to 0
        self.accel = GRAVITY_VEC.copy()
        if not self.wall_collide:
            if self.states[0]:
                self.accel.x = - ACCELERATION
                self.velocity.x -= 1.3
            elif self.states[1]:
                self.accel.x = ACCELERATION
                self.velocity.x += 1.3
        if self.jumping and self.is_on_ground:
            self.velocity.y = -19
            self.is_on_ground = False
        if not self.jumping and not self.is_on_ground:
            if self.velocity.y < -5:
                self.velocity.y = -5

        self.accel.x += self.velocity.x * FRICTION
        self.velocity += self.accel
        self.rect.move_ip(self.velocity + 0.5 * self.accel)

    def walk_counter(self):
        # find first item in self.states that is true
        # set idle state
        self.idle = self.states == [False, False] and not self.jumping
        if True in self.states:
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
        if self.death:
            screen.blit(player_death, self.rect)
        elif self.idle:
            if self.face_direction == LEFT:
                screen.blit(player_left_idle[self.stand_count // 7], self.rect)
            elif self.face_direction == RIGHT:
                screen.blit(player_right_idle[self.stand_count // 7], self.rect)
        else:
            # if moving left, right, or jumping
            if not self.jumping:
                if self.face_direction == LEFT:
                    screen.blit(player_left_walk[self.walk_count // 7], self.rect)
                elif self.face_direction == RIGHT:
                    screen.blit(player_right_walk[self.walk_count // 7], self.rect)
            else:
                if self.face_direction == LEFT:
                    screen.blit(player_left_jump, self.rect)
                elif self.face_direction == RIGHT:
                    screen.blit(player_right_jump, self.rect)
