import pygame

from src.constants import GAME_TITLE

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    screen = pygame.display.set_mode((1280, 720))
    from main_menu import MainMenu
    mainMenu = MainMenu(screen)
    mainMenu.run()
