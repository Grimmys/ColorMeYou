import pygame

from src.constants import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_ICON

if __name__ == "__main__":
    pygame.init()

    from src.scenes.main_menu import MainMenu

    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(GAME_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_menu = MainMenu(screen)
    main_menu.run()
