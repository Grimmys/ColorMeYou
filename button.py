# button class

import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
# could probably move this into constants since we will have an interact sound later
interact_sound = pygame.mixer.Sound('assets\sounds\interact_sound.mp3')
interact_sound.set_volume(0.4)

class Button():
    def __init__(self, image, screen, x, y, x_len, y_len):
        self.image = image
        self.screen = screen
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, x_len, y_len)
        self.played = False

    def detect_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.image, self.pos)
            if not self.played:
                interact_sound.play()
                self.played = True
        else:
            self.played = False
                
    # optional, only for start button, put within event loop
    def navigate(self, destination):
        self.destination = destination
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            page_instance = self.destination(screen)
            page_instance.run()
            del page_instance

