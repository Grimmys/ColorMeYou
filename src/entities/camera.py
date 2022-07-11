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

        # self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        left = 200
        top = 100
        width = SCREEN_WIDTH - 400
        height = SCREEN_HEIGHT - 200
        self.camera_rect = pygame.Rect(left, top, width, height)

    def box_target_camera(self, target):
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - 200
        self.offset.y = self.camera_rect.top - 100

    def custom_draw(self, player, moving_entities):
        self.box_target_camera(player)

        # active elements
        for entity in moving_entities:
            offset_pos = entity.rect.topleft - self.offset
            self.screen.blit(entity, offset_pos)
