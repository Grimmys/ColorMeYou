import pygame


class Entity:
    def __init__(self, x_coord, y_coord, width, height):
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.initial_rect = pygame.Rect(x_coord, y_coord, width, height)
        self.respawn_rect = self.initial_rect.copy()

    def draw(self, screen):
        pass

    # reset to init position
    def reset(self):
        self.rect = self.initial_rect.copy()

    # if player picked up cartridge, record position of rect
    def record(self, player, cartridge):
        if pygame.Rect.colliderect(player.rect, cartridge.rect):
            self.respawn_rect = self.rect.copy()

        return self.respawn_rect

    # respawn player at recorded rect
    def respawn(self):
        self.rect = self.respawn_rect.copy()
