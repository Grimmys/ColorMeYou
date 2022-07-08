# button class

import pygame

# could probably move this into constants since we will have an interact sound later
interact_sound = pygame.mixer.Sound("assets/sounds/interact_sound.mp3")
interact_sound.set_volume(0.4)


class Button:
    def __init__(self, image, screen, x_coord, y_coord, width, height):
        self.image = image
        self.screen = screen
        self.position = (x_coord, y_coord)
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.played = False

    def detect_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.image, self.position)
            if not self.played:
                interact_sound.play()
                self.played = True
        else:
            self.played = False

    # optional, only for start button, put within event loop
    def navigate(self, destination):
        self.destination = destination
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            page_instance = self.destination(self.screen)
            page_instance.run()
            return page_instance
        return None
