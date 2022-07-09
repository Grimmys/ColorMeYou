# camera

from src.entities.entity import Entity

class Camera(Entity):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__(x_coord, y_coord, width, height)