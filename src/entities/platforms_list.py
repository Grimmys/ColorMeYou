import pygame

from src.entities.platform import Platform
from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, MAGENTA, CYAN, BLACK, GREEN, YELLOW, BLUE, RED, SCREEN_WIDTH, \
    SCREEN_HEIGHT, INTERACT_SOUND, DELAY_BEFORE_NEXT_SCENE


death_line = Platform(BLACK, -1000, 2000, 10000, 20, True)

platforms = [
    # start stage
Platform(BLACK, 0, 540, 400, 1000, True),
    # 3 intro platforms
Platform(CYAN, 500, 440, 200, 40, True),
Platform(MAGENTA, 800, 340, 200, 40, False),
Platform(YELLOW, 1100, 240, 200, 40, False),
    # mini challenge 1
Platform(YELLOW, 1400, 140, 200, 40, True),
Platform(RED, 1400, -60, 40, 240, True),
    # end platform of pt 1, collect cartridge 1
Platform(BLACK, 1800, 100, 600, 1000, True),
    # start of pt 2, rainbow road
Platform(BLUE, 2400, 100, 200, 20, True),
Platform(RED, 2600, 100, 200, 20, True),
Platform(GREEN, 2800, 100, 200, 20, True),
Platform(BLUE, 3000, 100, 200, 20, True),
Platform(RED, 3200, 100, 200, 20, True),
Platform(GREEN, 3400, 100, 200, 20, True),
    # drop down platform and wall platform, plus lil ladders
    # collect cartridge 2
Platform(BLACK, 2400, 700, 2300, 1000, True),
Platform(BLACK, 3600, 100, 400, 250, True),
    # ladders
Platform(MAGENTA, 4200, 550, 100, 20, True),
Platform(CYAN, 4200, 400, 100, 20, True),
Platform(MAGENTA, 4200, 250, 100, 20, True),
Platform(YELLOW, 4200, 100, 100, 20, True),
    # and a support wall/platform
Platform(BLACK, 4300, 100, 3000, 1000, True),

    # part 3, go up !!!
Platform(CYAN, 4440, 0, 200, 40, True),
Platform(YELLOW, 4740, -180, 200, 40, True),
Platform(CYAN, 4440, -360, 200, 40, True),
Platform(YELLOW, 4740, -540, 200, 40, True),
Platform(CYAN, 4440, -720, 200, 40, True),
    # collect cartridge 3 here
Platform(MAGENTA, 4740, -900, 600, 40, True),
    # put paper here
    # part 4
Platform(BLACK, 7300, 700, 100, 20, True),
    # to win game, fall off on purpose to respawn at an earlier cartridge


death_line]