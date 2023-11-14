#!/usr/bin/env python3

"""
Module to start and stop drumming when the touch sensor is pressed.
This file must be run on the robot.
"""
 
import brickpi3
from utils.brick import TouchSensor, wait_ready_sensors, BP , Motor
import time



TOUCH_SENSOR = TouchSensor(3)

BP = brickpi3.BrickPi3()
#AUX_MOTOR = BP.PORT_A
POWER_LIMIT = 80
SPEED_LIMIT = 500
wait_ready_sensors() # Note: Touch sensors actually have no initialization time
MOTOR = Motor("A")


def toggle_drums(): #starts or stops motor
    
    "Start drumming"
    try:
        while not TOUCH_SENSOR.is_pressed():
            pass
        while True:
            angle = 360
            MOTOR.set_dps=1000
            MOTOR.set_limits(POWER_LIMIT,SPEED_LIMIT)
            MOTOR.set_position_relative(angle)
            time.sleep(0.01)
            #if toggle == 0:
                #continue
                        
    except KeyboardInterrupt:
        BP.reset_all()
                

# def TS_pressed():
#     "In an infinite loop, when the touch sensor is pressed, start or stop the drums depending on the drumON field"
#     try:
#         while True:
#             if TOUCH_SENSOR.is_pressed():
#                 toggle_drums()
#                 time.sleep(0.5)
#                 
#     except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
#         exit()
# 

if __name__=='__main__':
    while not TOUCH_SENSOR.is_pressed():
            pass 
    toggle_drums()