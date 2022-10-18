# Write your code here :-)
from digitalio import DigitalInOut, Direction, Pull
import board
import pulseio
import time
from adafruit_simplemath import map_range
from math import floor

pulses = DigitalInOut(board.D0)
pulses.direction = Direction.INPUT
pulses.pull = Pull.DOWN

PHASE_DELAY = 2100

while True:
    #get duty cycle
    while not pulses.value:
        pass
    start = time.monotonic_ns()
    while pulses.value:
        pass
    end = time.monotonic_ns()
    in_width = floor((end - start)/1000)
    #deadpoint centre for joystick
    if in_width > 1460 and in_width < 1590:
        out_width = 1520
    #max out forward
    elif in_width >= 1590:
        out_width = floor(map_range(in_width,1590,2100,1590,1920))
    #max out reverse
    else:
        out_width = floor(map_range(in_width,1460,980,1460,1120))
    print(str(out_width))
    #time.sleep((PHASE_DELAY - in_width))/10000
    #time.sleep(.1)
