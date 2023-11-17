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





def forward_mvmt():
        
    stop = False
    left_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    right_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    while True:
        
        sleep(0.1)
        left_wheel.set_position_relative(45)
        sleep(0.04)
        print("rotating left")
        right_wheel.set_position_relative(45)
        sleep(0.04)
        print("rotating right")
        
        color_data_R = color_sensor_right.get_rgb()
        color_data_L = color_sensor_left.get_rgb()
        
        norm_data_R = normalization.normalize(color_data_R)
        norm_data_L = normalization.normalize(color_data_L)
        
        color_right = normalization.determine_color(norm_data_R)
        color_left = normalization.determine_color(norm_data_L)
        
        print(color_right, color_left)
        print(stop)
        
        if (color_left == "Green" and color_right == "Green"):
            stop = True
            
        if (color_left == "Red" or color_left == "Blue"):
            left_wheel.set_position_relative(3)
            
        if (color_right == "Red" or color_right == "Blue"):
            right_wheel.set_position_relative(3)
        
        if (stop == True and color_left == "Green" and color_right == "Green"):
            sleep(0.2)
            break




        
def backward_mvmt():
    left_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    right_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    while True:
        
        sleep(0.1)
        left_wheel.set_position_relative(-45)
        sleep(0.04)
        print("rotating left")
        right_wheel.set_position_relative(-45)
        sleep(0.04)
        print("rotating right")
        
        color_data_R = color_sensor_right.get_rgb()
        color_data_L = color_sensor_left.get_rgb()
        
        norm_data_R = normalization.normalize(color_data_R)
        norm_data_L = normalization.normalize(color_data_L)
        
        color_right = normalization.determine_color(norm_data_R)
        color_left = normalization.determine_color(norm_data_L)
        
        print(color_right, color_left)
        print('stop')
            
        if (color_left == "Red" or color_left == "Blue"):
            left_wheel.set_position_relative(3)
            
        if (color_right == "Red" or color_right == "Blue"):
            right_wheel.set_position_relative(3)
        
        if (color_left == "Green" and color_right == "Green"):
            sleep(0.2)
            break



    

def turn_left():
    left_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    right_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    while True:
        sleep(0.1)
        right_wheel.set_position_relative(45)
        sleep(0.04)
        left_wheel.set_position_relative(-12)
        print("turning left")
        
        color_data_R = color_sensor_right.get_rgb()
        color_data_L = color_sensor_left.get_rgb()
        
        norm_data_R = normalization.normalize(color_data_R)
        norm_data_L = normalization.normalize(color_data_L)
        
        color_right = normalization.determine_color(norm_data_R)
        color_left = normalization.determine_color(norm_data_L)
        
        print(color_right, color_left)
        
        if (color_right == "Red" or color_right == "Blue"):
            print("HIT BLUE")
            right_wheel.set_position_relative(-10)
            break
    




def turn_right():
    left_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    right_wheel.set_limits(POWER_LIMIT,SPEED_LIMIT)
    while True:
        sleep(0.05)
        left_wheel.set_position_relative(50)
        sleep(0.04)
        right_wheel.set_position_relative(-12)
        print("turning right")
        
        color_data_R = color_sensor_right.get_rgb()
        color_data_L = color_sensor_left.get_rgb()
        
        norm_data_R = normalization.normalize(color_data_R)
        norm_data_L = normalization.normalize(color_data_L)
        
        color_right = normalization.determine_color(norm_data_R)
        color_left = normalization.determine_color(norm_data_L)
        
        print(color_right, color_left)
        
        if (color_left == "Red" or color_left == "Blue"):
            print("HIT BLUE")
            right_wheel.set_position_relative(10)
            left_wheel.set_position_relative(-30)
            break




        
if __name__ == "__main__":
    print('hello')

    