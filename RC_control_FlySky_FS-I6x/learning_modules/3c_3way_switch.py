'''Basic RC Analog input Control
Outputs two toggle switches. SWB and SWC.
You must first set Ch 5/6 to SWB and SWC respectively on the controller first.
SWB is a 2 way toggle switch
SWC is a 3 way toggle switch.

'''

from digitalio import DigitalInOut, Direction, Pull
import board
import time
import rc

#init channel pin as a digital input. Defaults to a FALSE reading, so we must pull down.

#SwC
ch6 = DigitalInOut(board.D8)
ch6.direction = Direction.INPUT
ch6.pull = Pull.DOWN

while True:
    # read switches
    ch6_cur = rc.read_3way_switch(ch6)

    print(" SwC: " + str(ch6_cur)) # print current switch state



