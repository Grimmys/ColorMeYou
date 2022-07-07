import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    from main_menu import MainMenu
    mainMenu = MainMenu(screen)
    mainMenu.run()
