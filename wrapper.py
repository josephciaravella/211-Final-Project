import normalization
import pathfinding
import brickpi3
from utils.brick import TouchSensor, wait_ready_sensors, BP , Motor, EV3ColorSensor
from time import sleep

BP = brickpi3.BrickPi3()
#AUX_MOTOR = BP.PORT_A
POWER_LIMIT = 200
SPEED_LIMIT = 200
wait_ready_sensors() 
left_wheel = Motor("C")
right_wheel = Motor("B")
color_sensor_left = EV3ColorSensor(3)
color_sensor_right = EV3ColorSensor(2)          
FIRE_POSITION_DICT = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6}
orientation = "up"
curr_pos = [0,0]



def determine_move(curr_pos, next_pos):
    """
    Determines the move direction based on the current position and the next position.

    Parameters:
    - curr_pos (tuple): A tuple representing the current position (x, y).
    - next_pos (tuple): A tuple representing the next position (x, y).

    Returns:
    - move (str): A string representing the direction of the move. Possible values are "north", "south", "east", or "west".
    """
    # Calculate the change in x and y coordinates
    delta_x = next_pos[0] - curr_pos[0]
    delta_y = next_pos[1] - curr_pos[1]

    # Combine the changes into a tuple representing the move coordinates
    move_coord = (delta_x, delta_y)

    # Define a dictionary mapping move coordinates to direction strings
    move_dict = {(0, 1): "north", (0, -1): "south", (1, 0): "east", (-1, 0): "west"}

    # Retrieve the direction string based on the move coordinates
    move = move_dict[move_coord]

    # Return the determined move direction
    return move


def navigation(path):
    """
    Navigates a path in a grid based on specified moves, updating the current position and orientation.

    Parameters:
    - path (list of tuples): A list of tuples representing the path to navigate. Each tuple is a coordinate (x, y).

    Returns:
    - orientation (string): A string representing the orientation of the robot once it reaches the end of its path

    Notes:
    - The function modifies the current position and orientation based on the given path.
    - The orientation is initially set to "up" and is updated as the navigation progresses.
    - The function includes placeholder comments for specific actions to be taken at each step in the grid.
    """

    
    
    i=0
    while (i+1 <= len(path)):
        move = determine_move(curr_pos, path[i+1])


        if move == "west":
            curr_pos[0] -= 1
            if orientation == "left":
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "right":
                # rotate left x2
                pathfinding.turn_left()
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "up":
                # rotate left
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "down":
                # rotate right
                pathfinding.turn_right()
                # go straight
                pathfinding.forward_mvmt()

            orientation = "left"
            

        if move == "east":
            curr_pos[0] += 1
            if orientation == "left":
                # rotate left x2
                pathfinding.turn_left()
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "right":
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "up":
                # rotate right
                pathfinding.turn_right()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "down":
                # rotate left
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()

            orientation = "right"
        

        if move == "north":
            curr_pos[1] += 1
            if orientation == "left":
                # rotate right
                pathfinding.turn_right()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "right":
                # rotate left
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "up":
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "down":
                # rotate left x2
                pathfinding.turn_left()
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()

            orientation = "up"

            
        if move == "south":
            curr_pos[1] -= 1
            if orientation == "left":
                # rotate left
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "right":
                # rotate right
                pathfinding.turn_right()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "up":
                # rotate left x2
                pathfinding.turn_left()
                pathfinding.turn_left()
                # go straight
                pathfinding.forward_mvmt()
            elif orientation == "down":
                # go straight
                pathfinding.forward_mvmt()

            orientation = "down"

        i+=1

    return orientation



def delivery(input_string):
    input = input_string.split(',')
    fire1 = FIRE_POSITION_DICT[input[2]]
    fire2 = FIRE_POSITION_DICT[input[5]]
    fire3 = FIRE_POSITION_DICT[input[8]]

    fire_pos1 = (input[0],input[1])
    fire_pos2 = (input[3],input[4])
    fire_pos3 = (input[6],input[7])

    #call shortest_path(grid, (0,0), fire_pos1, fire_pos2, fire_pos3)
