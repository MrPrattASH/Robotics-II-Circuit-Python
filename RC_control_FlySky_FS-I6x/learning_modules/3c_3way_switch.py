'''Basic RC Analog input Control
Outputs two toggle switches: SWC channel 6.
SWC is a 3 way toggle switch.

'''

import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1 = board.D0, ch2 = board.D1, ch3 = None, ch4 = None, ch5 =board.D2, ch6 =board.D3)

# Main code
while True:
    # Read channels
    channel_6 = rc.read_channel(6)
    if channel_6 is not None: # must not be None to do something with the output
        print("Channel 6:", channel_6)
    
    # sleep for 20ms at the end of our loop, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)




