import pygame


class Entity:
    def __init__(self, x_coord, y_coord, width, height):
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.initial_rect = pygame.Rect(x_coord, y_coord, width, height)
    def draw(self, screen):
        pass
    # reset to init position
    def reset(self):
        self.rect = self.initial_rect.copy()
    # if player picked up cartridge, record position of rect
    def record(self, player, cartridge):
        if pygame.Rect.collideRect(player.rect, cartridge.rect):
            self.respawn = self.rect.copy()
    # respawn player at recorded rect
    def respawn(self):
        self.rect = self.respawn.copy()
