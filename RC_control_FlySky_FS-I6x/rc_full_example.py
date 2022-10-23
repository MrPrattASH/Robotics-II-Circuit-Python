"""Basic RC Analog input Control Full example
Full RC example for all 6 channels populated.

Note, likely you will not use Channels 3/4 as analog inputs, though they exist for example purposes.
"""

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import rc

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

#moving average lists, we'll only ever have 2 values here.
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

    #update moving average lists
    rc.upd_mov_avg(x_moving, x_joy)
    rc.upd_mov_avg(y_moving, y_joy)

    #check if new list item was equal to the last sensor addition
    if rc.all_equal(x_moving):
        #update the motor output
        x_out = x_moving[0]
    if rc.all_equal(y_moving):
        y_out = y_moving[0]

    print("swB: " + str(sw_c) + " swC: " + str(sw_c) +  " X_Joy: " + str(x_out) + " Y:Joy " + str(y_out))
