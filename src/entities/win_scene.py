# win scene
import pygame

from src.scenes.scene import Scene
from src.scenes.scene import MainMenu
# import win condition
from src.gui.load_sprites import endscreens

class WinScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
    
    def draw(self):
        super().draw()
        # check win condition here
        self.screen.blit(endscreens[0], (0, 0))
    
    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_scene = self.start_button.navigate(MainMenu)
        
