import math
from app.utils import COMPASS_TO_DIR

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

    def print_rover(self):
        print (self.position[0], self.position[1], self.compass)


class Plateau (object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size
