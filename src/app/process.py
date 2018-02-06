import re

def read_file(path):
    input_file = open(path,'r')
    data = input_file.readlines()
    input_file.close()
    return data


def process_data(data):
    plateau = []
    deployment = {}
    movements = {}

    for line in data:
        # Check for Plateau size
        prog = re.compile('[Plateau]+\s*[a-zA-Z]*\s*[:]\s*([0-9]+)[x]([0-9]+)')
        result = prog.match(line)
        if result:
            plateau_x, plateau_y = int(result.group(1)), int(result.group(2))
            plateau = [plateau_x, plateau_y]
            continue

        # Check for rovers deployment
        prog = re.compile('[Rover]+\s*([0-9]+)\s*[a-zA-Z]*\s*[a-zA-Z]*\s*[:]\s*([0-9]+)\s*([0-9]+)\s*([a-zA-Z])')
        result = prog.match(line)
        if result:
            rover_id, rover_x, rover_y, rover_compass = int(result.group(1)), int(result.group(2)), int(result.group(3)), str(result.group(4))
            # print(rover_id, rover_x, rover_y, rover_compass)
            deployment[rover_id] = [rover_x, rover_y, rover_compass]
            continue

        # Check for rovers movement
        prog = re.compile('[Rover]+\s*([0-9]+)\s*[a-zA-Z]*\s*[:]\s*([A-Z]+)')
        result = prog.match(line)
        if result:
            rover_id, rover_mov = int(result.group(1)), str(result.group(2))
            # print(rover_id, rover_mov)
            movements[rover_id] = rover_mov
            continue
        
    return plateau, deployment, movements
