# upload sprites here
# animation cycles are stored in lists based on action and direction
# some standalones also included 

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
mc_ss = SpriteSheet('assets\images\mc_ss.png')
misc_ss = SpriteSheet('assets\images\misc_ss.png')
lit_buttons = SpriteSheet('assets\images\lit_buttons.png')

# right facing idle
mc_right_idle = []
mc_right_idle_coords = []
for i in range(0, 7):
    mc_right_idle_coords.append((i * 96, 0, i * 96 + 96, 480))
# print(mc_right_idle_coords)
mc_ss.load_strip(mc_right_idle_coords, mc_right_idle, 96, 480)

# right facing walk
mc_right_walk = []
mc_right_walk_coords = []
for i in range(0, 4):
    mc_right_walk_coords.append((i * 96, 480, i * 96 + 96, 240))
# print(mc_right_walk_coords)
mc_ss.load_strip(mc_right_walk_coords, mc_right_walk, 96, 480)

# right jump
mc_right_jump_rect = (0, 240, 96, 360)
mc_right_jump = mc_ss.image_at(mc_right_jump_rect, 96, 480)

# right interact
mc_r_interact_rect = (96, 240, 192, 360)
mc_r_interact = mc_ss.image_at(mc_r_interact_rect, 96, 480)

#----------------------------------------------------------------

# left idle
mc_left_idle = []
mc_left_idle_coords = []
for i in range(0, 7):
    mc_left_idle_coords.append((i * 96, 360, i * 96 + 96, 480))
# print (mc_left_idle_coords)
mc_ss.load_strip(mc_left_idle_coords, mc_left_idle, 96, 480)

# left facing walk
mc_left_walk = []
mc_left_walk_coords = []
for i in range(0, 4):
    mc_left_walk_coords.append((i * 96, 480, i * 96 + 96, 600))
mc_ss.load_strip(mc_left_walk_coords, mc_left_walk, 96, 480)

# left jump
mc_lj_rect = (96, 600, 192, 780)
mc_lj = mc_ss.image_at(mc_lj_rect, 96, 480)

# left interact
mc_l_interact_rect = (0, 600, 96, 780)
mc_l_interact = mc_ss.image_at(mc_l_interact_rect, 96, 480)

#------------------------------------------------------

# death
mc_death_rect = (0, 780, 96, 840)
mc_death = mc_ss.image_at(mc_death_rect, 96, 480)

#------------------------------------------------------

# papier-san

paper = []
paper_coords = []
for i in range(0, 3):
    paper_coords.append((i * 80, 0, i * 80 + 80, 96))
misc_ss.load_strip(paper_coords, paper, 80, 96)

#CMY toggler, c - 0, m - 1, y - 2

toggles = []
toggles_coords = []
for i in range(0, 3):
    toggles_coords.append((i * 200, 96, i * 200 + 200, 96 + 212))
misc_ss.load_strip(toggles_coords, toggles, 200, 212)

# cat blob
enemy = []
enemy_coords = []
for i in range(0, 2):
    enemy_coords.append((i * 480, 212 + 96, i * 480 + 480, 212 + 96 + 80))
misc_ss.load_strip(enemy_coords, enemy, 480, 80)

# cartridges, c - 0, m - 1, y - 2
cartridges = []
cartridge_coords = []
for i in range(0, 3):
    cartridge_coords.append((i * 23, 212 + 96 + 80, i * 23 + 23, 212 + 96 + 80 + 21))
misc_ss.load_strip(cartridge_coords, cartridges, 23, 21)

# main menu buttons
start_button_rect = (0, 0, 568, 112)
start_button_img = lit_buttons.image_at(start_button_rect, 568, 112)

settings_button_rect = (0, 112, 568, 146)
settings_button_img = lit_buttons.image_at(settings_button_rect, 568, 112)