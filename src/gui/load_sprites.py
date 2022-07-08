# upload sprites here
# animation cycles are stored in lists based on action and direction
# some standalones also included 

import pygame


class SpriteSheet:
    def __init__(self, filename):
        """Load the sheet."""
        self.filename = filename
        self.spritesheet = pygame.image.load(filename)

    # load from list of rects
    def load_strip(self, rects, lis, dimx, dimy):
        for rect in rects:
            sprite = pygame.Surface((dimx, dimy), pygame.SRCALPHA)
            sprite.blit(self.spritesheet, (0, 0), rect)
            lis.append(sprite)

    # load single img
    def image_at(self, rect, dimx, dimy):
        sprite = pygame.Surface((dimx, dimy), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), rect)
        return sprite


# load in
player_ss = SpriteSheet("assets/images/mc_ss.png")
misc_ss = SpriteSheet("assets/images/misc_ss.png")
lit_buttons = SpriteSheet("assets/images/lit_buttons.png")

# right facing idle
player_right_idle = []
player_right_idle_coords = []
for i in range(0, 7):
    player_right_idle_coords.append((i * 96, 0, i * 96 + 96, 120))

player_ss.load_strip(player_right_idle_coords, player_right_idle, 96, 120)

# right facing walk
player_right_walk = []
player_right_walk_coords = []
for i in range(0, 4):
    player_right_walk_coords.append((i * 96, 120, i * 96 + 96, 240))

player_ss.load_strip(player_right_walk_coords, player_right_walk, 96, 120)

# right jump
player_right_jump_rect = (0, 240, 96, 360)
player_right_jump = player_ss.image_at(player_right_jump_rect, 96, 120)

# right interact
player_r_interact_rect = (96, 240, 192, 360)
player_r_interact = player_ss.image_at(player_r_interact_rect, 96, 120)

# ----------------------------------------------------------------

# left idle
player_left_idle = []
player_left_idle_coords = []
for i in range(0, 7):
    player_left_idle_coords.append((i * 96, 360, i * 96 + 96, 480))

player_ss.load_strip(player_left_idle_coords, player_left_idle, 96, 120)

# left facing walk
player_left_walk = []
player_left_walk_coords = []
for i in range(0, 4):
    player_left_walk_coords.append((i * 96, 480, i * 96 + 96, 600))
player_ss.load_strip(player_left_walk_coords, player_left_walk, 96, 120)

# left jump
player_left_jump_rect = (96, 600, 192, 780)
player_left_jump = player_ss.image_at(player_left_jump_rect, 96, 120)

# left interact
player_l_interact_rect = (0, 600, 96, 780)
player_l_interact = player_ss.image_at(player_l_interact_rect, 96, 120)

# ------------------------------------------------------

# death
player_death_rect = (0, 780, 96, 840)
player_death = player_ss.image_at(player_death_rect, 96, 120)

# ------------------------------------------------------

# papier-san

paper = []
paper_coords = []
for i in range(0, 3):
    paper_coords.append((i * 80, 0, i * 80 + 80, 96))
misc_ss.load_strip(paper_coords, paper, 80, 96)

# CMY toggler, c - 0, m - 1, y - 2

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

# backgrounds

backgrounds = []

cyan_bg = pygame.image.load("assets/images/c_mode_bg.png")
magenta_bg = pygame.image.load("assets/images/y_mode_bg.png")
yellow_bg = pygame.image.load("assets/images/y_mode_bg.png")

backgrounds.append(cyan_bg, magenta_bg, yellow_bg)