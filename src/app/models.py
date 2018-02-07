import math
import numpy as np
from app.utils import COMPASS_TO_DIR, DIR_TO_COMPASS, array_to_string

class Storage(object):
    def __init__(self, plateau, deployment, movements):
        self.plateau = plateau
        self.deployment = deployment
        self.movements = movements

    def set_plateau(self, size):
        self.plateau = size

    def get_plateau(self):
        return self.plateau

    def set_deployment(self, deployment):
        self.deployment = deployment

    def get_deployment(self):
        return self.deployment

    def set_movements(self, movements):
        self.movements = movements

    def get_movements(self):
        return self.movements


class Rover (object):
    def __init__(self, deployment):
        self.position = [deployment[0], deployment[1]]
        self.direction = COMPASS_TO_DIR[deployment[2]]
        self.compass = deployment[2]

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def set_compass(self, compass):
        self.compass = compass

    def get_compass(self):
        return self.compass

    def rotate(self, alpha):
        dir_x, dir_y = self.direction
        x = int(math.cos(alpha) * dir_x - math.sin(alpha) * dir_y)
        y = int(math.sin(alpha) * dir_x + math.cos(alpha) * dir_y)

        self.direction = np.array([x, y])

        new_compass = array_to_string(self.direction)
        self.compass = DIR_TO_COMPASS[new_compass]


    def forward(self, plateau):
        dir_x, dir_y = self.direction
        pos_x, pos_y = self.position
        new_pos = [dir_x + pos_x, dir_y + pos_y]

        size_x, size_y = plateau.get_size()

        if new_pos[0] in range(0, size_x + 1) and new_pos[1] in range(0, size_y + 1):
            self.position = new_pos


    def move(self, action, plateau):
        action = action.upper()
        for acc in action:
            if acc == 'L':
                self.rotate(math.pi/2)
            elif acc == 'R':
                self.rotate(-math.pi/2)
            elif acc == 'M':
                self.forward(plateau)


class Plateau (object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size
