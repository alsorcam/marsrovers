""" Controller of actions """
from app.models import Rover, Storage, Plateau

rovers = {}
plateau = Plateau([0,0])

def init(storage):
  """ Load the rovers from the input data """
  # Get data from storage
  plateau.set_size(storage.get_plateau())
  deployment = storage.get_deployment()
  movements = storage.get_movements()  

  # Create dict of rovers
  for key in deployment.keys():
    if rover_id not in rovers.keys():
      rovers[rover_id] = rover
    else:
      print ("Cannot add rover", rover_id)

  # Print input data
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
  for key in rovers.keys():
    rovers[key].move(movements[key], plateau)


def print_positions():
  """ Print the positions of the rovers """
  for key in rovers.keys():
    rover = rovers[key]
    print ("Rover", key, "position:", rover.get_position()[0], rover.get_position()[1], rover.get_compass())
