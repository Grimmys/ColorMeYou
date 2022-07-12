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
Platform(CYAN, 1400, 140, 200, 40, True),
Platform(BLUE, 1400, -60, 40, 400, True),
    # end platform of pt 1
Platform(BLACK, 1800, 100, 600, 1000, True), death_line]