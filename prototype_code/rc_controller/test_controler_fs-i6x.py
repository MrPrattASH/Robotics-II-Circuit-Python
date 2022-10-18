# Write your code here :-)
'''test RC controller code'''

import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn

#init Ch 1, Left/right
lr_joystick = AnalogIn(board.A1)

#init Ch 2, Throttle
thr_joystick = AnalogIn(board.A2)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    print(get_voltage(lr_joystick))
    time.sleep(0.2)
