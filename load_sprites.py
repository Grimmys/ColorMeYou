# upload sprites here

import pygame
import sys

class SpriteSheet:
    def __init__(self, filename):
        """Load the sheet."""
        self.filename = filename
        self.spritesheet = pygame.image.load(filename)
    #load from list of rects
    def load_strip(self, rects, lis, dimx, dimy):
        for rect in rects:
            sprite = pygame.Surface((dimx, dimy), pygame.SRCALPHA)
            sprite.blit(self.spritesheet,(0, 0), rect)
            lis.append(sprite)
    #load single img
    def image_at(self, rect, dimx, dimy):
        sprite = pygame.Surface((dimx, dimy), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), rect)
        return sprite

# load in
mc_ss = SpriteSheet('assets\mc_ss.png')
misc_ss = SpriteSheet('assets\misc_ss.png')

# right facing idle
mc_ri = []
mc_ri_coords = []
for i in range(0, 7):
    mc_ri_coords.append((i * 24, 0, i * 24 + 24, 30))
# print(mc_ri_coords)
mc_ss.load_strip(mc_ri_coords, mc_ri, 24, 30)

# right facing walk
mc_rw = []
mc_rw_coords = []
for i in range(0, 4):
    mc_rw_coords.append((i * 24, 30, i * 24 + 24, 60))
# print(mc_rw_coords)
mc_ss.load_strip(mc_rw_coords, mc_rw, 24, 30)

# right jump
mc_rj_rect = (0, 60, 24, 90)
mc_rj = mc_ss.image_at(mc_rj_rect, 24, 30)

# right interact
mc_r_interact_rect = (24, 60, 48, 90)
mc_r_interact = mc_ss.image_at(mc_r_interact_rect, 24, 30)

#----------------------------------------------------------------

# left idle
mc_li = []
mc_li_coords = []
for i in range(0, 7):
    mc_li_coords.append((i * 24, 90, i * 24 + 24, 120))
# print (mc_li_coords)
mc_ss.load_strip(mc_li_coords, mc_li, 24, 30)

# left facing walk
mc_lw = []
mc_lw_coords = []
for i in range(0, 4):
    mc_lw_coords.append((i * 24, 120, i * 24 + 24, 150))
mc_ss.load_strip(mc_lw_coords, mc_lw, 24, 30)

# left jump
mc_lj_rect = (24, 150, 48, 180)
mc_lj = mc_ss.image_at(mc_lj_rect, 24, 30)

# left interact
mc_l_interact_rect = (0, 150, 24, 180)
mc_l_interact = mc_ss.image_at(mc_l_interact_rect, 24, 30)

#------------------------------------------------------

# death
mc_death_rect = (0, 180, 24, 210)
mc_death = mc_ss.image_at(mc_death_rect, 24, 30)

#------------------------------------------------------

# papier-san

pp = []
pp_coords = []
for i in range(0, 3):
    pp_coords.append((i * 20, 0, i * 20 + 20, 24))
misc_ss.load_strip(pp_coords, pp, 20, 24)

#CMY toggler, c - 0, m - 1, y - 2

toggles = []
toggles_coords = []
for i in range(0, 3):
    toggles_coords.append((i * 50, 24, i * 50 + 50, 24 + 53))
misc_ss.load_strip(toggles_coords, toggles, 50, 53)

# cat blob

enemy = []


