""" Script for object utils """

# Get the direction from a cardinal point
COMPASS_TO_DIR = {
  'N': [0, 1],
  'S': [0, -1],
  'E': [1, 0],
  'W': [-1, 0]
}

# Get the cardinal point from the direction data
DIR_TO_COMPASS = {
  '0 1': 'N',
  '0 -1': 'S',
  '1 0': 'E',
  '-1 0': 'W'
}

def array_to_string(array):
  """ Convert an array to a string (only coordenates, without brackets or commas)"""
  x, y = array
  return ''.join([str(x), ' ', str(y)])
