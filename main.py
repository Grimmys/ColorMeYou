import pygame

from src.constants import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_ICON

if __name__ == "__main__":
    pygame.init()

    from src.scenes.main_menu import MainMenu

    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(GAME_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_is_active = True
    clock = pygame.time.Clock()

    active_scene = MainMenu(screen)
    active_scene.run()

    while game_is_active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_is_active = False
            active_scene.process_event(event)
        active_scene.draw()
        active_scene.update()
        if active_scene.next_scene is not None:
            active_scene.timer_until_next_scene -= 1
            if active_scene.timer_until_next_scene <= 0:
                active_scene = active_scene.next_scene
        pygame.display.update()
