""" This code is for after the initial GoBuilda FTC Kit Build test:

The robot has basic functions for:
forward
backwards
left/right
90*, 180*, 360*

Lift arm up, down

RoboClaw is programmed:
Button mode 1 (RC)
Option 4 (Tank Style) - intended state to run this program
"""

import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo
from adafruit_simplemath import map_range
from math import floor
import rc
from arcade_drive import servo_duty_cycle, arcade_drive

# init DC motors as pwm objects
motor1 = pwmio.PWMOut(board.D0, frequency=50)
motor2 = pwmio.PWMOut(board.D1, frequency=50)

# motor speed commands
STOP = 1.520
FULL_FORWARD = 1.920  # +400us (microseconds)
FULL_REVERSE = 1.120  # -400us (microseconds)

# init RC Controller
# R joystick LR
ch1 = DigitalInOut(board.D5)
ch1.direction = Direction.INPUT
ch1.pull = Pull.DOWN

# R joystick UD
ch2 = DigitalInOut(board.D6)
ch2.direction = Direction.INPUT
ch2.pull = Pull.DOWN

# SwB 2 way toggle
ch5 = DigitalInOut(board.D7)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

# SwC 3 way toggle
ch6 = DigitalInOut(board.D8)
ch6.direction = Direction.INPUT
ch6.pull = Pull.DOWN

#We initialize both at 0 to start the program in a dead-stop position
#moving average lists
x_moving = [0,0]
y_moving = [0,0]
#actual output to motors
x_out = 0
y_out = 0

while True:
    # Get RC Readings
    sw_c = rc.read_3way_switch(ch6)
    sw_b = rc.read_2way_switch(ch5)
    y_joy = rc.read_analog(ch2)
    x_joy = rc.read_analog(ch1)

    #update moving average list with most current reading
    rc.upd_mov_avg(x_moving, x_joy)
    rc.upd_mov_avg(y_moving, y_joy)

    #filter lists with all equal. If no high-spike readings, update x_out value
    if rc.all_equal(x_moving):
        x_out = x_moving[0]
    if rc.all_equal(y_moving):
        y_out = y_moving[0]

    #drive motors using true output values
    arcade_drive(x_out, y_out, motor1, motor2)
