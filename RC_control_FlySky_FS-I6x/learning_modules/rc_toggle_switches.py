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
#SwB
ch5 = DigitalInOut(board.D7)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

#SwC
ch6 = DigitalInOut(board.D8)
ch6.direction = Direction.INPUT
ch6.pull = Pull.DOWN

def read_3way_switch(pin):
    """
    Reads a value from an analog channel on an RC reciever for a 3 way switch.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout, input, and pull.down
    :returns: if 2 way switch, 0, 1, if 3 way switch, 0,1,2

    """
    # start low value
    start = time.monotonic_ns()
    # time_monotonic call stops a program break if no signal is recieved
    while not pin.value:
        pass
    # get high value
    start = time.monotonic_ns()
    while pin.value:
        pass
    end = time.monotonic_ns()

    # convert time.monotonic into a nice 4 digit duty_cycle value
    in_width = floor((end - start) / 1000)

    # bottom position
    if in_width <= 1200:
        out_value = 0
    # top position
    elif in_width >= 1800:
        out_value = 2
    # mid position
    else:
        out_value = 1
    #Allow for next PWM cycle frequency to read correctly
    #If we don't sleep, we'll start 'out of sync' with the PWM cycle
    #and only return LOW values. Best trial and error reliable value returned 1.51ms wait time.
    time.sleep(0.00151)
    return out_value

def read_2way_switch(pin):
    """
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout, input, and pull.down
    :returns: if 2 way switch, 0, 1, if 3 way switch, 0,1,2

    """
    # start low value
    start = time.monotonic_ns()
    # time_monotonic call stops a program break if no signal is recieved
    while not pin.value:
        pass
    # get high value
    start = time.monotonic_ns()
    while pin.value:
        pass
    end = time.monotonic_ns()

    # convert time.monotonic into a nice 4 digit duty_cycle value
    in_width = floor((end - start) / 1000)

    # switch in up position (OFF)
    if in_width <= 1500:
        out_value = 0
    else:
        out_value = 1

    #Allow for next PWM cycle frequency to read correctly
    #If we don't sleep, we'll start 'out of sync' with the PWM cycle
    #and only return LOW values. Best trial and error reliable value returned 1.51ms wait time.
    time.sleep(0.00151)
    return out_value

while True:
    # read switches
    ch5_cur = read_2way_switch(ch5)
    ch6_cur = read_3way_switch(ch6)

    print("SwB: " + str(ch5) + " SwC: " + str(ch6))


