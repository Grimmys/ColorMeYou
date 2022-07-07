import pygame

<<<<<<< HEAD
from src.constants import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_ICON
=======
from main_menu import MainMenu
from src.constants import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT
>>>>>>> 1c3ea7a9cf31c759bee3a34cbfe4f708ac631643

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
<<<<<<< HEAD
    pygame.display.set_icon(GAME_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    from main_menu import MainMenu
    mainMenu = MainMenu(screen)
    mainMenu.run()
=======
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_menu = MainMenu(screen)
    main_menu.run()
>>>>>>> 1c3ea7a9cf31c759bee3a34cbfe4f708ac631643
