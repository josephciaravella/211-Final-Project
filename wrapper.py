import normalization
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



def determine_move(prev_pos, curr_pos, direction):


    return move, direction;


def navigation(path):
    direction = "up"
    curr_pos = [0,0]
    move = determine_move()

    if move == "left":
        curr_pos[0] -= 1
        if direction == "left":
            # go straight
        elif direction == "right":
            # rotate left x2
            # go straight
        elif direction == "up":
            # rotate left
            # go straight
        elif direction == "down":
            # rotate right
            # go straight
        


    if move == "right":
        curr_pos[0] += 1
        if direction == "left":
            # rotate left x2
            # go straight
        elif direction == "right":
            # go straight
        elif direction == "up":
            # rotate right
            # go straight
        elif direction == "down":
            # rotate left
            # go straight
    
    if move == "up":
        curr_pos[1] += 1
        #go straight 
        #curr_pos[1] += 1



def delivery(input_string):
    input = input_string.split(',')
    fire1 = FIRE_POSITION_DICT[input[2]]
    fire2 = FIRE_POSITION_DICT[input[5]]
    fire3 = FIRE_POSITION_DICT[input[8]]

    fire_pos1 = (input[0],input[1])
    fire_pos2 = (input[3],input[4])
    fire_pos3 = (input[6],input[7])

    #call shortest_path(grid, (0,0), fire_pos1, fire_pos2, fire_pos3)