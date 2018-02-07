# Mars Rovers
First approach to the solution of the problem Mars Rovers.



# Problem
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their
on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position and location is represented by a combination of x and y coordinates and a letter representing one of the four cardinal compass points. The plateau is
divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively,
without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).
Input: The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the
second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the rover’s orientation.

Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.


## Test input
Plateau size: 5x5

Rover 1 deploy zone: 1 2 N

Rover 1 movement: LMLMLMLMM

Rover 2 deploy zone: 3 3 E

Rover 2 movement: MMRMMRMRRM


## Expected Output
Rover 1 position: 1 3 N

Rover 2 position: 5 1 E



# Solution
The solution is based in 5 different scripts:

- controller.py where the actions are defined such as moving the rover or printing information.

- main.py where the application is started and initialized.

- models.py where the objects are specified as classes.

- process.py where the input data is processed at first.

- utils.py where the utilities are, such as the conversion of the cardinal point to a 2D vector representing its direction.


## Setup
Install Python 3.6.4

Install all dependent pip packages: 
```
pip install -r requirements.txt
```


## Running
Access to the src folder and execute the main.py script:
```
cd src
python main.py ../test_input.txt
```


## Testing
To run the tests:
```
cd src
python -m unittest discover test
```
