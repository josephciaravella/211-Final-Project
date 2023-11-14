import brickpi3
from utils.brick import TouchSensor, wait_ready_sensors, BP , Motor
import time

BP = brickpi3.BrickPi3()
#AUX_MOTOR = BP.PORT_A
POWER_LIMIT = 80
SPEED_LIMIT = 60
wait_ready_sensors() 
left_wheel = Motor(2)
right_wheel = Motor(3)
color_sensor = EV3ColorSensor("C")

def forward_mvmt():
    
    
    
def backward_mvmt():
    
    

def turn_left():
    
    
    
def turn_right():