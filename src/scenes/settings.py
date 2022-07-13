import pygame
from src.constants import INTERACT_SOUND, BLACK

from src.gui.button import Button
from src.scenes.scene import Scene
from src.entities.entity import Entity

SETTINGS_SCENE_IMAGE = pygame.image.load("assets/images/settings_pop_up.png")
CLOSE_BUTTON_IMAGE = pygame.image.load("assets/images/cross.png")
CLOSE_BUTTON_DISTANCE_TO_BORDER = 20
LEFT_ARROW_IMAGE = pygame.image.load("assets/images/left_arrow.png")
RIGHT_ARROW_IMAGE = pygame.image.load("assets/images/right_arrow.png")

INCREMENT_LENGTH = 50.5


class Levels(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)
        # default level
        self.level = 4
    
    def increment_up(self):
        if self.level + 1 < 9:
            self.level += 1
            self.rect.width += INCREMENT_LENGTH
    
    def increment_down(self):
        if self.level - 1 > -1:
            self.level -= 1
            self.rect.width -= INCREMENT_LENGTH

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect) 
        

class Settings(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.position = (self.screen.get_width() // 2 - SETTINGS_SCENE_IMAGE.get_width() // 2,
                         self.screen.get_height() // 2 - SETTINGS_SCENE_IMAGE.get_height() // 2)
        self.close_button = Button(CLOSE_BUTTON_IMAGE, screen,
                                   SETTINGS_SCENE_IMAGE.get_width() - CLOSE_BUTTON_IMAGE.get_width() -
                                   CLOSE_BUTTON_DISTANCE_TO_BORDER + self.position[0],
                                   CLOSE_BUTTON_DISTANCE_TO_BORDER + self.position[1],
                                   CLOSE_BUTTON_IMAGE.get_width(), CLOSE_BUTTON_IMAGE.get_height())
        self.scene_bound_to_close_button = None
        self.decrease_button = Button(LEFT_ARROW_IMAGE, screen, 375, 422, 29, 40)
        self.increase_button = Button(RIGHT_ARROW_IMAGE, screen, 872, 422, 29, 40)
        self.levels_bar = Levels(440, 435, 4 * INCREMENT_LENGTH, 15)

    def draw(self):
        super().draw()
        self.screen.blit(SETTINGS_SCENE_IMAGE, self.position)
        self.screen.blit(self.close_button.image, self.close_button.rect)
        if self.decrease_button.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.decrease_button.image, self.decrease_button.rect)
        if self.increase_button.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.increase_button.image, self.increase_button.rect)
        
        self.levels_bar.draw(self.screen)

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.decrease_button.rect.collidepoint(pygame.mouse.get_pos()):
                INTERACT_SOUND.play()
                self.levels_bar.increment_down()
                
            if self.increase_button.rect.collidepoint(pygame.mouse.get_pos()):
                INTERACT_SOUND.play()
                self.levels_bar.increment_up()

            if self.close_button.rect.collidepoint(pygame.mouse.get_pos()):
                INTERACT_SOUND.play()
                self.next_scene = self.scene_bound_to_close_button(self.screen)
                self.next_scene.run()

