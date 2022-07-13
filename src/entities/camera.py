# camera

import pygame

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.entity import Entity

vec = pygame.math.Vector2


class Camera(Entity):
    def __init__(self, x_coord, y_coord, width, height, screen):
        super().__init__(x_coord, y_coord, width, height)
        self.screen = screen

        self.offset = vec(0, 0)

        self.half_w = SCREEN_WIDTH // 2
        self.half_h = SCREEN_HEIGHT // 2

        self.camera_borders = {'left': 640, 'right': 640, 'top': 360, 'bottom': 360}
        left = self.camera_borders['left']
        top = self.camera_borders['top']
        width = SCREEN_WIDTH - 2 * self.camera_borders['left']
        height = SCREEN_HEIGHT - 2 * self.camera_borders['top']
        self.camera_rect = pygame.Rect(left, top, width, height)

    def box_target_camera(self, target, moving_entities):

        self.offset = vec(0, 0)
        self.collide = vec(False, False)

        # check collision
        if target.rect.left <= self.camera_rect.left or target.rect.right >= self.camera_rect.right:
            self.collide.x = True
        else:
            self.collide.x = False

        if target.rect.top >= self.camera_rect.top or target.rect.bottom <= self.camera_rect.bottom:
            self.collide.y = True
        else:
            self.collide.y = False

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top > self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom < self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        if self.collide.x:
            self.offset.x = self.camera_rect.left - self.camera_borders['left']
        if self.collide.y:
            self.offset.y = self.camera_rect.top - self.camera_borders['top']

        # self.offset = vec(0, 0)

        for entity in moving_entities:
            entity.rect.x -= self.offset.x
            entity.rect.y -= self.offset.y

    def center_camera(self, target, moving_entities):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

        for entity in moving_entities:
            entity.rect.x -= self.offset.x
            entity.rect.y -= self.offset.y
