import brickpi3
from utils.brick import wait_ready_sensors, BP , Motor
import time

BP = brickpi3.BrickPi3()
POWER_LIMIT=80
SPEED_LIMIT=500
wait_ready_sensors() 
LMOTOR=Motor('D')
RMOTOR=Motor('A')
def motor_start():
    angle=360
    try:
        LMOTOR.set_limits(POWER_LIMIT,SPEED_LIMIT)
        LMOTOR.set_position_relative(angle)
        RMOTOR.set_limits(POWER_LIMIT,SPEED_LIMIT)
        RMOTOR.set_position_relative(angle)
        time.sleep(1)
    except KeyboardInterrupt:
        BP.reset_all()
    
if __name__=='__main__':
    motor_start()