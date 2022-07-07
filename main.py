import pygame

from src.constants import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_ICON

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(GAME_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    from main_menu import MainMenu
    mainMenu = MainMenu(screen)
    mainMenu.run()
