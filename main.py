import pygame

from main_menu import MainMenu
from src.constants import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_menu = MainMenu(screen)
    main_menu.run()
