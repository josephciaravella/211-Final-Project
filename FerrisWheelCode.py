import brickpi3
from utils.brick import TouchSensor, wait_ready_sensors, BP , Motor
import time

BP = brickpi3.BrickPi3()
#AUX_MOTOR = BP.PORT_A
POWER_LIMIT = 80
SPEED_LIMIT = 60
wait_ready_sensors() 
MOTOR = Motor("D")


def motor_start(position):
#     pos_mod_6 = position % 6
#     curr_position = 0
#     difference = position - curr_position
    angle =  position * 61
    neg_angle = 365.5 - angle
    # angle2 =  position2 * 61
    #neg_angle2 = 365.5 - angle2
    # angle3 =  position3 * 61
    #neg_angle3 = 365.5 - angle3
    try:
        #Ftype = eval(input('Enter Fire Type:'))
         
        #MOTOR.set_dps=1000
        MOTOR.set_limits(POWER_LIMIT,SPEED_LIMIT)
        MOTOR.set_position_relative(angle)
        time.sleep(10) #take into account time to push off block
        print("rotation 1")
    except KeyboardInterrupt:
        BP.reset_all()
    
    finally:
        #push block out
        MOTOR.set_limits(POWER_LIMIT,SPEED_LIMIT)
        MOTOR.set_position_relative(neg_angle)
        print("rotation 2")
        
    
if __name__=='__main__':
    motor_start(5)