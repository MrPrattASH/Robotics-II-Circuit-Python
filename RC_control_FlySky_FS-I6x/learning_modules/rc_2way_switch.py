'''Basic RC Analog input Control
Outputs one toggle switches. SWB.
You must first set Ch 5 to SWB on the transmitter first.
SWB is a 2 way toggle switch

'''

from digitalio import DigitalInOut, Direction, Pull
import board
import rc

#init channel pin as a digital input. Defaults to a FALSE reading, so we must pull down.
#SwB
ch5 = DigitalInOut(board.D7)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

while True:
    # read switches
    ch5_cur = rc.read_2way_switch(ch5)

    # print current switch state
    print("SwB: " + str(ch5_cur))


