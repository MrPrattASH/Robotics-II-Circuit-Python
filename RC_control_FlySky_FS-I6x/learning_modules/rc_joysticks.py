"""Basic RC Analog input Control
Outputs an analog channel duty cycle rating in 0>100.
50 is the deadpoint. 0 is miniumum, 100 is maximum.

"""

import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1 = board.D0, ch2 = board.D1, ch3 = None, ch4 = None, ch5 =board.D2, ch6 =board.D3)

# Main code
while True:
    # Read channels
    channel_1 = rc.read_channel(1)
    channel_2 = rc.read_channel(2)
    if channel_1 is not None and channel_2 is not None: # must not be None to do something with the output
        print("1: ", channel_1, "2: ", channel_2)
    
    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)