""" Controller of actions """
import math
import numpy as np
from app.models import Rover, Storage, Plateau
from app.utils import DIR_TO_COMPASS, array_to_string

rovers = {}
plateau = Plateau([0,0])

def init(storage):
  """ Load the rovers from the input data """
  plateau.set_size(storage.get_plateau())
  deployment = storage.get_deployment()
  movements = storage.get_movements()  

  for key in deployment.keys():
    add_rover(key, Rover(deployment[key]))

  print ("Plateau size:", storage.get_plateau())

  for key in rovers.keys():
    rover = rovers[key]
    pos = deployment[key]
    mov = movements[key]
    print ("Rover", key, "deploy zone:", pos)
    print ("Rover", key, "movement:", mov)


def run(storage):
  """ Move the rovers according to the input data """
  movements = storage.get_movements()

  for key in movements.keys():
    move(key, movements[key])


def add_rover(rover_id, rover):
  """ Add a rover to the list """
  if rover_id not in rovers.keys():
    rovers[rover_id] = rover
  else:
    print ("Cannot add rover", rover_id)


def move(rover_id, action):
  """ Move a rover depending on a specified action """
  rover = rovers[rover_id]
  for acc in action:
    if acc == 'L':
        rotate(rover, math.pi/2)
    elif acc == 'R':
        rotate(rover, -math.pi/2)
    elif acc == 'M':
        forward(rover)


def rotate(rover, alpha):
    """ Rotate the direction of the rover """
    dir_x, dir_y = rover.get_direction()
    x = int(math.cos(alpha) * dir_x - math.sin(alpha) * dir_y)
    y = int(math.sin(alpha) * dir_x + math.cos(alpha) * dir_y)

    new_dir = np.array([x, y])
    rover.set_direction(new_dir)

    new_compass = array_to_string(new_dir)
    rover.set_compass(DIR_TO_COMPASS[new_compass])


def forward(rover):
    """ Move forward the rover in a certain direction """
    dir_x, dir_y = rover.get_direction()
    pos_x, pos_y = rover.get_position()
    new_pos = [dir_x + pos_x, dir_y + pos_y]

    size_x, size_y = plateau.get_size()

    if new_pos[0] in range(0, size_x + 1) and new_pos[1] in range(0, size_y + 1):
      rover.set_position(new_pos)
    else:
      new_compass = array_to_string(rover.get_direction())
      print ("Cannot move in this direction: ", DIR_TO_COMPASS[new_compass])


def print_positions():
  """ Print the positions of the rovers """
  for key in rovers.keys():
    rover = rovers[key]
    print ("Rover", key, "position:", rover.get_position()[0], rover.get_position()[1], rover.get_compass())
