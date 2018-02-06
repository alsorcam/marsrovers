""" Main executable """
import sys
import app.controller as ctrl
from app.process import read_file, process_data
from app.models import Storage

def main():
    if len(sys.argv) < 2:
        print("InvalidSyntax: Provide a filename")
        exit()
    else:
        run_app(sys.argv[1])


def run_app(filename):
    # Read the data from the input file
    data = read_file(filename)

    # Get the data separated
    plateau, deployment, movements = process_data(data)

    # Create a storage for the data
    storage = Storage(plateau, deployment, movements)

    # Create the rovers and display input data
    print ("---------------------------")
    print ("          INPUT            ")
    print ("---------------------------")
    ctrl.init(storage)

    # Move the rovers
    ctrl.run(storage)

    # Print the output data
    print ("---------------------------")
    print ("          OUTPUT           ")
    print ("---------------------------")
    ctrl.print_positions()


if __name__ == '__main__':
    main()
