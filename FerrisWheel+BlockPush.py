import brickpi3
from utils.brick import wait_ready_sensors, BP, Motor
import time

BP=brickpi3.BrickPi3()
POWER_LIMIT=80
SPEED_LIMIT=80
SPEED_LIMIT_BP=800
wait_ready_sensors()
MOTORFW=Motor('A')
MOTORBP=Motor('D')

#def proj_input(x):
 #   input(x)
    

def MOTOR_start(pos1,pos2,pos3):
    #NOTE: THE CUBE AT THE BOTTOM WILL ALWAYS BE THE GREEN ONE
    if (pos1==0):
        angle1=0
        full_rot1=0
    elif (pos1==1):
        angle1 = 61.5
        full_rot1=301 
    elif (pos1 ==2):
        angle1 = 122
        full_rot1=242
    elif (pos1==3): 
        angle1 = 182
        full_rot1=182.5
    elif (pos1==4):
        angle1 = 242.5
        full_rot1=121
    elif (pos1==5):
        angle1 = 301
        full_rot1=65.5
    if (pos2==0):
        angle2=0
        full_rot2=0
    elif (pos2==1):
        angle2 = 64.5
        full_rot2=301
    elif (pos2 ==2):
        angle2 = 122.5
        full_rot2=242.5
    elif (pos2==3): #184 is fine both ways
        angle2 = 184
        full_rot2=183
    elif (pos2==4):
        angle2 = 243
        full_rot2=121
    elif (pos2==5):
        angle2 = 300
        full_rot2=66
    if (pos3==0):
        angle3=0
        full_rot3=0
    elif (pos3==1):
        angle3 = 64
        full_rot3=301
    elif (pos3 ==2):
        angle3 = 123
        full_rot3=243.5
    elif (pos3==3): #184 is fine both ways
        angle3 = 182.5
        full_rot3=183
    elif (pos3==4):
        angle3 = 243
        full_rot3=121
    elif (pos3==5):
        angle3 = 300.5
        full_rot3=64
    

    try:
        MOTORFW.set_limits(POWER_LIMIT,SPEED_LIMIT)
        MOTORFW.set_position_relative(angle1)
        time.sleep(6)
    except KeyboardInterrupt:
        BP.reset_all()
    anglePUSH=-360
    angleRETRACT=360
    try:
        MOTORBP.set_limits(POWER_LIMIT,SPEED_LIMIT_BP)
        MOTORBP.set_position_relative(anglePUSH)
        time.sleep(1.5)
    except KeyboardInterrupt:
        BP.reset_all()
    try:
        MOTORBP.set_position_relative(angleRETRACT)
        time.sleep(1.5)
    except KeyboardInterrupt:
        BP.reset_all()
    finally:
        MOTORFW.set_position_relative(full_rot1)
        time.sleep(6)
    try:
        MOTORFW.set_limits(POWER_LIMIT,SPEED_LIMIT)
        MOTORFW.set_position_relative(angle2)
        time.sleep(6)
    except KeyboardInterrupt:
        BP.reset_all()
    try:
        MOTORBP.set_limits(POWER_LIMIT,SPEED_LIMIT_BP)
        MOTORBP.set_position_relative(anglePUSH)
        time.sleep(1.5)
    except KeyboardInterrupt:
        BP.reset_all()
    try:
        MOTORBP.set_position_relative(angleRETRACT)
        time.sleep(1.5)
    except KeyboardInterrupt:
        BP.reset_all()
    finally:
        MOTORFW.set_position_relative(full_rot2)
        time.sleep(6)
    try:
        MOTORFW.set_limits(POWER_LIMIT,SPEED_LIMIT)
        MOTORFW.set_position_relative(angle3)
        time.sleep(6)
    except KeyboardInterrupt:
        BP.reset_all()
    try:
        MOTORBP.set_limits(POWER_LIMIT,SPEED_LIMIT_BP)
        MOTORBP.set_position_relative(anglePUSH)
        time.sleep(1.5)
    except KeyboardInterrupt:
        BP.reset_all()
    try:
        MOTORBP.set_position_relative(angleRETRACT)
        time.sleep(1.5)
    except KeyboardInterrupt:
        BP.reset_all()
    finally:
        MOTORFW.set_position_relative(full_rot3)
        time.sleep(6)

if __name__=='__main__':
    MOTOR_start(4,5,2) #1,4,5