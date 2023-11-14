import brickpi3
from utils.brick import wait_ready_sensors, BP , Motor
import time

BP = brickpi3.BrickPi3()
POWER_LIMIT=80
SPEED_LIMIT=500
wait_ready_sensors() 
MOTOR=Motor('D')

def motor_start():
    angle=360
    try:
        MOTOR.set_limits(POWER_LIMIT,SPEED_LIMIT)
        MOTOR.set_position_relative(angle)
        time.sleep(1)
    except KeyboardInterrupt:
        BP.reset_all()
    
if __name__=='__main__':
    motor_start()