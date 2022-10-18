# Write your code here :-)
# Write your code here :-)
'''Basic RC Analog input Control
Outputs two toggle switches. SWB and SWC.
You must first set Ch 5/6 to SWB and SWC respectively on the controller first.
SWB is a 2 way toggle switch
SWC is a 3 way toggle switch.

'''

from digitalio import DigitalInOut, Direction, Pull
import board
import time
from math import floor

#init channel pin as a digital input. Defaults to a FALSE reading, so we must pull down.
#PWM will input as low/high values
ch5 = DigitalInOut(board.D0)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

def read_switch_ch(pin, three_way_switch = False):
    '''
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout, input, and pull.down
    :three_way_switch: Bool: Default is a 2-way toggle switch. If true, will return a 3way toggle switch
    :returns: if 2 way switch, 0, 1, if 3 way switch, 0,1,2

    '''
    #start low value
    while not pin.value:
        pass
    #get high value
    start = time.monotonic_ns()
    while pin.value:
        pass
    end = time.monotonic_ns()

    #convert time.monotonic into a nice 4 digit duty_cycle value
    in_width = floor((end - start)/1000)

    #2-way switch
    if not three_way_switch:
        #switch in up position (OFF)
        if in_width <= 1500:
            out_value = 0
        else:
            out_value = 1

    #3-way switch
    else:
        #bottom position
        if in_width <= 1200:
            out_value = 0
        #top position
        elif in_width >=1800:
            out_value = 2
        #mid position
        else:
            out_value = 1
    return out_value
    #note, do NOT introduce a sleep into this code, or it will output odd numbers.

while True:
    print(read_switch_ch(ch5,three_way_switch = True))
    #time.sleep(.2)

